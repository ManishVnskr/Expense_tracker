package com.expensetracker.dto;

import com.expensetracker.model.Budget;
import lombok.Builder;
import lombok.Data;

import java.math.BigDecimal;

@Data
@Builder
public class BudgetProgressResponse {
    private Budget budget;
    private BigDecimal spent;
    private BigDecimal remaining;
    private Double percentage;
    private AlertStatus alertStatus;
    private Long daysRemaining;
    
    public enum AlertStatus {
        OK,         // < threshold
        WARNING,    // >= threshold but < 100%
        EXCEEDED    // >= 100%
    }
}
