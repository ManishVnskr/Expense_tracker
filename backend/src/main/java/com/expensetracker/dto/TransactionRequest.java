package com.expensetracker.dto;

import com.expensetracker.model.Transaction;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDate;

@Data
public class TransactionRequest {
    
    @NotNull(message = "Amount is required")
    @Positive(message = "Amount must be positive")
    private BigDecimal amount;
    
    @NotNull(message = "Type is required")
    private Transaction.TransactionType type;
    
    private Long categoryId;
    
    private String description;
    
    @NotNull(message = "Transaction date is required")
    private LocalDate transactionDate;
    
    private String paymentMethod;
    
    private String[] tags;
}
