package com.expensetracker.service;

import com.expensetracker.dto.BudgetProgressResponse;
import com.expensetracker.dto.BudgetRequest;
import com.expensetracker.model.Budget;
import com.expensetracker.model.Transaction;
import com.expensetracker.repository.BudgetRepository;
import com.expensetracker.repository.TransactionRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class BudgetService {

    private final BudgetRepository budgetRepository;
    private final TransactionRepository transactionRepository;
    private final UserService userService;

    public BudgetService(BudgetRepository budgetRepository, 
                        TransactionRepository transactionRepository,
                        UserService userService) {
        this.budgetRepository = budgetRepository;
        this.transactionRepository = transactionRepository;
        this.userService = userService;
    }

    public List<BudgetProgressResponse> getBudgets(Long householdId) {
        userService.validateHouseholdAccess(householdId);
        List<Budget> budgets = budgetRepository.findByHouseholdIdOrderByStartDateDesc(householdId);
        return budgets.stream()
                .map(budget -> calculateProgress(householdId, budget))
                .collect(Collectors.toList());
    }

    public BudgetProgressResponse getBudgetProgress(Long householdId, Long budgetId) {
        userService.validateHouseholdAccess(householdId);
        Budget budget = budgetRepository.findById(budgetId)
                .orElseThrow(() -> new RuntimeException("Budget not found"));
        
        if (!budget.getHouseholdId().equals(householdId)) {
            throw new RuntimeException("Access denied");
        }
        
        return calculateProgress(householdId, budget);
    }

    @Transactional
    public Budget createBudget(Long householdId, BudgetRequest request) {
        userService.validateHouseholdAccess(householdId);
        
        if (request.getEndDate().isBefore(request.getStartDate())) {
            throw new RuntimeException("End date must be after start date");
        }
        
        Budget budget = Budget.builder()
                .householdId(householdId)
                .name(request.getName())
                .amount(request.getAmount())
                .periodType(request.getPeriodType())
                .startDate(request.getStartDate())
                .endDate(request.getEndDate())
                .alertThreshold(request.getAlertThreshold() != null ? request.getAlertThreshold() : 80)
                .build();
        
        return budgetRepository.save(budget);
    }

    @Transactional
    public Budget updateBudget(Long householdId, Long budgetId, BudgetRequest request) {
        userService.validateHouseholdAccess(householdId);
        
        Budget budget = budgetRepository.findById(budgetId)
                .orElseThrow(() -> new RuntimeException("Budget not found"));
        
        if (!budget.getHouseholdId().equals(householdId)) {
            throw new RuntimeException("Access denied");
        }
        
        if (request.getEndDate().isBefore(request.getStartDate())) {
            throw new RuntimeException("End date must be after start date");
        }
        
        budget.setName(request.getName());
        budget.setAmount(request.getAmount());
        budget.setPeriodType(request.getPeriodType());
        budget.setStartDate(request.getStartDate());
        budget.setEndDate(request.getEndDate());
        budget.setAlertThreshold(request.getAlertThreshold() != null ? request.getAlertThreshold() : 80);
        
        return budgetRepository.save(budget);
    }

    @Transactional
    public void deleteBudget(Long householdId, Long budgetId) {
        userService.validateHouseholdAccess(householdId);
        
        Budget budget = budgetRepository.findById(budgetId)
                .orElseThrow(() -> new RuntimeException("Budget not found"));
        
        if (!budget.getHouseholdId().equals(householdId)) {
            throw new RuntimeException("Access denied");
        }
        
        budgetRepository.deleteById(budgetId);
    }

    private BudgetProgressResponse calculateProgress(Long householdId, Budget budget) {
        // Calculate total expenses in budget period
        BigDecimal spent = transactionRepository.sumByHouseholdIdAndTypeAndDateRange(
                householdId,
                Transaction.TransactionType.EXPENSE,
                budget.getStartDate(),
                budget.getEndDate()
        );
        
        if (spent == null) {
            spent = BigDecimal.ZERO;
        }
        
        BigDecimal remaining = budget.getAmount().subtract(spent);
        double percentage = spent.divide(budget.getAmount(), 4, RoundingMode.HALF_UP)
                .multiply(BigDecimal.valueOf(100))
                .doubleValue();
        
        // Determine alert status
        BudgetProgressResponse.AlertStatus alertStatus;
        if (percentage >= 100) {
            alertStatus = BudgetProgressResponse.AlertStatus.EXCEEDED;
        } else if (percentage >= budget.getAlertThreshold()) {
            alertStatus = BudgetProgressResponse.AlertStatus.WARNING;
        } else {
            alertStatus = BudgetProgressResponse.AlertStatus.OK;
        }
        
        // Calculate days remaining
        LocalDate today = LocalDate.now();
        long daysRemaining = 0;
        if (today.isBefore(budget.getEndDate())) {
            daysRemaining = ChronoUnit.DAYS.between(today, budget.getEndDate());
        }
        
        return BudgetProgressResponse.builder()
                .budget(budget)
                .spent(spent)
                .remaining(remaining)
                .percentage(percentage)
                .alertStatus(alertStatus)
                .daysRemaining(daysRemaining)
                .build();
    }
}
