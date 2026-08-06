package com.expensetracker.controller;

import com.expensetracker.model.Category;
import com.expensetracker.service.CategoryService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/households/{householdId}/categories")
public class CategoryController {

    private final CategoryService categoryService;

    public CategoryController(CategoryService categoryService) {
        this.categoryService = categoryService;
    }

    @GetMapping
    public ResponseEntity<List<Category>> getCategories(@PathVariable Long householdId) {
        return ResponseEntity.ok(categoryService.getCategories(householdId));
    }

    @PostMapping
    public ResponseEntity<Category> createCategory(
            @PathVariable Long householdId,
            @Valid @RequestBody Category category) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(categoryService.createCategory(householdId, category));
    }

    @DeleteMapping("/{categoryId}")
    public ResponseEntity<Void> deleteCategory(
            @PathVariable Long householdId,
            @PathVariable Long categoryId) {
        categoryService.deleteCategory(householdId, categoryId);
        return ResponseEntity.noContent().build();
    }
}
