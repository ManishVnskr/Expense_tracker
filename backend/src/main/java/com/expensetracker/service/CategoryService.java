package com.expensetracker.service;

import com.expensetracker.model.Category;
import com.expensetracker.repository.CategoryRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class CategoryService {

    private final CategoryRepository categoryRepository;
    private final UserService userService;

    public CategoryService(CategoryRepository categoryRepository, UserService userService) {
        this.categoryRepository = categoryRepository;
        this.userService = userService;
    }

    public List<Category> getCategories(Long householdId) {
        userService.validateHouseholdAccess(householdId);
        return categoryRepository.findByHouseholdIdOrderByTypeAscNameAsc(householdId);
    }

    @Transactional
    public Category createCategory(Long householdId, Category category) {
        userService.validateHouseholdAccess(householdId);
        category.setHouseholdId(householdId);
        category.setIsDefault(false);
        return categoryRepository.save(category);
    }

    @Transactional
    public void deleteCategory(Long householdId, Long categoryId) {
        userService.validateHouseholdAccess(householdId);
        Category category = categoryRepository.findById(categoryId)
                .orElseThrow(() -> new RuntimeException("Category not found"));
        
        if (category.getIsDefault()) {
            throw new RuntimeException("Cannot delete default categories");
        }
        
        if (!category.getHouseholdId().equals(householdId)) {
            throw new RuntimeException("Access denied");
        }
        
        categoryRepository.deleteById(categoryId);
    }
}
