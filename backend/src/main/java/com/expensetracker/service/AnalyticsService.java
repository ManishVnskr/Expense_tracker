package com.expensetracker.service;

import com.expensetracker.dto.AnalyticsDto;
import com.expensetracker.dto.BudgetProgressResponse;
import com.expensetracker.model.Category;
import com.expensetracker.model.Transaction;
import com.expensetracker.repository.CategoryRepository;
import com.expensetracker.repository.TransactionRepository;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class AnalyticsService {

    private final TransactionRepository transactionRepository;
    private final CategoryRepository categoryRepository;
    private final BudgetService budgetService;
    private final UserService userService;

    public AnalyticsService(TransactionRepository transactionRepository,
                           CategoryRepository categoryRepository,
                           BudgetService budgetService,
                           UserService userService) {
        this.transactionRepository = transactionRepository;
        this.categoryRepository = categoryRepository;
        this.budgetService = budgetService;
        this.userService = userService;
    }

    public AnalyticsDto.DashboardResponse getDashboard(Long householdId) {
        userService.validateHouseholdAccess(householdId);
        
        // Current month range
        LocalDate startOfMonth = LocalDate.now().withDayOfMonth(1);
        LocalDate endOfMonth = LocalDate.now().withDayOfMonth(LocalDate.now().lengthOfMonth());
        
        // Calculate totals
        BigDecimal totalExpense = transactionRepository.sumByHouseholdIdAndTypeAndDateRange(
                householdId, Transaction.TransactionType.EXPENSE, startOfMonth, endOfMonth);
        BigDecimal totalIncome = transactionRepository.sumByHouseholdIdAndTypeAndDateRange(
                householdId, Transaction.TransactionType.INCOME, startOfMonth, endOfMonth);
        
        totalExpense = totalExpense != null ? totalExpense : BigDecimal.ZERO;
        totalIncome = totalIncome != null ? totalIncome : BigDecimal.ZERO;
        BigDecimal balance = totalIncome.subtract(totalExpense);
        
        // Expenses by category
        List<Transaction> expenses = transactionRepository.findByHouseholdIdAndDateRange(
                householdId, startOfMonth, endOfMonth).stream()
                .filter(t -> t.getType() == Transaction.TransactionType.EXPENSE)
                .collect(Collectors.toList());
        
        Map<Long, BigDecimal> categoryTotals = expenses.stream()
                .filter(t -> t.getCategoryId() != null)
                .collect(Collectors.groupingBy(
                        Transaction::getCategoryId,
                        Collectors.reducing(BigDecimal.ZERO, Transaction::getAmount, BigDecimal::add)
                ));
        
        Map<Long, Category> categoryMap = categoryRepository.findAllById(categoryTotals.keySet())
                .stream()
                .collect(Collectors.toMap(Category::getId, c -> c));
        
        final BigDecimal finalTotalExpense = totalExpense;
        List<AnalyticsDto.CategorySummary> expensesByCategory = categoryTotals.entrySet().stream()
                .map(entry -> {
                    Category category = categoryMap.get(entry.getKey());
                    Double percentage = finalTotalExpense.compareTo(BigDecimal.ZERO) > 0
                            ? entry.getValue().divide(finalTotalExpense, 4, RoundingMode.HALF_UP)
                                    .multiply(BigDecimal.valueOf(100)).doubleValue()
                            : 0.0;
                    return AnalyticsDto.CategorySummary.builder()
                            .categoryId(entry.getKey())
                            .categoryName(category != null ? category.getName() : "Unknown")
                            .amount(entry.getValue())
                            .percentage(percentage)
                            .build();
                })
                .sorted((a, b) -> b.getAmount().compareTo(a.getAmount()))
                .limit(5)
                .collect(Collectors.toList());
        
        // Recent transactions
        List<Transaction> recentTransactions = transactionRepository
                .findByHouseholdIdOrderByTransactionDateDesc(householdId, PageRequest.of(0, 10))
                .getContent();
        
        List<AnalyticsDto.TransactionSummary> recentSummaries = recentTransactions.stream()
                .map(t -> {
                    String categoryName = t.getCategoryId() != null && categoryMap.containsKey(t.getCategoryId())
                            ? categoryMap.get(t.getCategoryId()).getName()
                            : "Uncategorized";
                    return AnalyticsDto.TransactionSummary.builder()
                            .id(t.getId())
                            .amount(t.getAmount())
                            .type(t.getType().name())
                            .description(t.getDescription())
                            .transactionDate(t.getTransactionDate().toString())
                            .categoryName(categoryName)
                            .build();
                })
                .collect(Collectors.toList());
        
        // Active budgets
        List<BudgetProgressResponse> activeBudgets = budgetService.getBudgets(householdId).stream()
                .filter(b -> !b.getBudget().getEndDate().isBefore(LocalDate.now()))
                .limit(5)
                .collect(Collectors.toList());
        
        return AnalyticsDto.DashboardResponse.builder()
                .totalExpense(totalExpense)
                .totalIncome(totalIncome)
                .balance(balance)
                .expensesByCategory(expensesByCategory)
                .recentTransactions(recentSummaries)
                .activeBudgets(activeBudgets)
                .build();
    }

    public AnalyticsDto.TrendsResponse getTrends(Long householdId, int months) {
        userService.validateHouseholdAccess(householdId);
        
        LocalDate endDate = LocalDate.now();
        LocalDate startDate = endDate.minusMonths(months);
        
        List<Transaction> transactions = transactionRepository.findByHouseholdIdAndDateRange(
                householdId, startDate, endDate);
        
        // Group by month
        Map<YearMonth, List<Transaction>> expensesByMonth = transactions.stream()
                .filter(t -> t.getType() == Transaction.TransactionType.EXPENSE)
                .collect(Collectors.groupingBy(t -> YearMonth.from(t.getTransactionDate())));
        
        Map<YearMonth, List<Transaction>> incomeByMonth = transactions.stream()
                .filter(t -> t.getType() == Transaction.TransactionType.INCOME)
                .collect(Collectors.groupingBy(t -> YearMonth.from(t.getTransactionDate())));
        
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM");
        
        List<AnalyticsDto.MonthlyData> monthlyExpenses = new ArrayList<>();
        List<AnalyticsDto.MonthlyData> monthlyIncome = new ArrayList<>();
        
        for (int i = months - 1; i >= 0; i--) {
            YearMonth month = YearMonth.from(endDate.minusMonths(i));
            String monthStr = month.format(formatter);
            
            List<Transaction> monthExpenses = expensesByMonth.getOrDefault(month, Collections.emptyList());
            BigDecimal expenseTotal = monthExpenses.stream()
                    .map(Transaction::getAmount)
                    .reduce(BigDecimal.ZERO, BigDecimal::add);
            
            monthlyExpenses.add(AnalyticsDto.MonthlyData.builder()
                    .month(monthStr)
                    .amount(expenseTotal)
                    .transactionCount(monthExpenses.size())
                    .build());
            
            List<Transaction> monthIncome = incomeByMonth.getOrDefault(month, Collections.emptyList());
            BigDecimal incomeTotal = monthIncome.stream()
                    .map(Transaction::getAmount)
                    .reduce(BigDecimal.ZERO, BigDecimal::add);
            
            monthlyIncome.add(AnalyticsDto.MonthlyData.builder()
                    .month(monthStr)
                    .amount(incomeTotal)
                    .transactionCount(monthIncome.size())
                    .build());
        }
        
        // Category breakdown for the period
        Map<String, BigDecimal> categoryBreakdown = transactions.stream()
                .filter(t -> t.getType() == Transaction.TransactionType.EXPENSE && t.getCategoryId() != null)
                .collect(Collectors.groupingBy(
                        t -> {
                            Category category = categoryRepository.findById(t.getCategoryId()).orElse(null);
                            return category != null ? category.getName() : "Unknown";
                        },
                        Collectors.reducing(BigDecimal.ZERO, Transaction::getAmount, BigDecimal::add)
                ));
        
        return AnalyticsDto.TrendsResponse.builder()
                .monthlyExpenses(monthlyExpenses)
                .monthlyIncome(monthlyIncome)
                .categoryBreakdown(categoryBreakdown)
                .build();
    }
}
