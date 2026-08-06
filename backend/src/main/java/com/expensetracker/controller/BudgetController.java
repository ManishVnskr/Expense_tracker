package com.expensetracker.controller;

import com.expensetracker.dto.BudgetProgressResponse;
import com.expensetracker.dto.BudgetRequest;
import com.expensetracker.model.Budget;
import com.expensetracker.service.BudgetService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/households/{householdId}/budgets")
public class BudgetController {

    private final BudgetService budgetService;

    public BudgetController(BudgetService budgetService) {
        this.budgetService = budgetService;
    }

    @GetMapping
    public ResponseEntity<List<BudgetProgressResponse>> getBudgets(@PathVariable Long householdId) {
        return ResponseEntity.ok(budgetService.getBudgets(householdId));
    }

    @GetMapping("/{budgetId}")
    public ResponseEntity<BudgetProgressResponse> getBudgetProgress(
            @PathVariable Long householdId,
            @PathVariable Long budgetId) {
        return ResponseEntity.ok(budgetService.getBudgetProgress(householdId, budgetId));
    }

    @PostMapping
    public ResponseEntity<Budget> createBudget(
            @PathVariable Long householdId,
            @Valid @RequestBody BudgetRequest request) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(budgetService.createBudget(householdId, request));
    }

    @PutMapping("/{budgetId}")
    public ResponseEntity<Budget> updateBudget(
            @PathVariable Long householdId,
            @PathVariable Long budgetId,
            @Valid @RequestBody BudgetRequest request) {
        return ResponseEntity.ok(budgetService.updateBudget(householdId, budgetId, request));
    }

    @DeleteMapping("/{budgetId}")
    public ResponseEntity<Void> deleteBudget(
            @PathVariable Long householdId,
            @PathVariable Long budgetId) {
        budgetService.deleteBudget(householdId, budgetId);
        return ResponseEntity.noContent().build();
    }
}
