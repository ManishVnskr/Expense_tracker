package com.expensetracker.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;
import java.time.YearMonth;
import java.util.List;
import java.util.Map;

public class AnalyticsDto {

    @Data
    @Builder
    public static class DashboardResponse {
        private BigDecimal totalExpense;
        private BigDecimal totalIncome;
        private BigDecimal balance;
        private List<CategorySummary> expensesByCategory;
        private List<TransactionSummary> recentTransactions;
        private List<BudgetProgressResponse> activeBudgets;
    }

    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class CategorySummary {
        private Long categoryId;
        private String categoryName;
        private BigDecimal amount;
        private Double percentage;
    }

    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class TransactionSummary {
        private Long id;
        private BigDecimal amount;
        private String type;
        private String description;
        private String transactionDate;
        private String categoryName;
    }

    @Data
    @Builder
    public static class TrendsResponse {
        private List<MonthlyData> monthlyExpenses;
        private List<MonthlyData> monthlyIncome;
        private Map<String, BigDecimal> categoryBreakdown;
    }

    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class MonthlyData {
        private String month;  // Format: "2026-08"
        private BigDecimal amount;
        private Integer transactionCount;
    }
}
