package com.expensetracker.service;

import com.expensetracker.dto.LoginRequest;
import com.expensetracker.dto.LoginResponse;
import com.expensetracker.dto.RegisterRequest;
import com.expensetracker.dto.UserResponse;
import com.expensetracker.model.Category;
import com.expensetracker.model.Household;
import com.expensetracker.model.User;
import com.expensetracker.repository.CategoryRepository;
import com.expensetracker.repository.HouseholdRepository;
import com.expensetracker.repository.UserRepository;
import com.expensetracker.security.JwtTokenProvider;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

@Service
public class AuthService {

    private final UserRepository userRepository;
    private final HouseholdRepository householdRepository;
    private final CategoryRepository categoryRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtTokenProvider jwtTokenProvider;

    public AuthService(UserRepository userRepository,
                      HouseholdRepository householdRepository,
                      CategoryRepository categoryRepository,
                      PasswordEncoder passwordEncoder,
                      JwtTokenProvider jwtTokenProvider) {
        this.userRepository = userRepository;
        this.householdRepository = householdRepository;
        this.categoryRepository = categoryRepository;
        this.passwordEncoder = passwordEncoder;
        this.jwtTokenProvider = jwtTokenProvider;
    }

    @Transactional
    public UserResponse register(RegisterRequest request) {
        // Check if email already exists
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new RuntimeException("Email already exists");
        }

        // Create user
        User user = User.builder()
                .email(request.getEmail())
                .passwordHash(passwordEncoder.encode(request.getPassword()))
                .fullName(request.getFullName())
                .build();
        user = userRepository.save(user);

        // Auto-create household
        Household household = Household.builder()
                .name(request.getFullName() + "'s Household")
                .currency("USD")
                .userId(user.getId())
                .build();
        household = householdRepository.save(household);

        // Create default categories
        createDefaultCategories(household.getId());

        return UserResponse.fromUser(user, household.getId());
    }

    public LoginResponse login(LoginRequest request) {
        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new RuntimeException("Invalid email or password"));

        if (!passwordEncoder.matches(request.getPassword(), user.getPasswordHash())) {
            throw new RuntimeException("Invalid email or password");
        }

        Household household = householdRepository.findByUserId(user.getId())
                .orElseThrow(() -> new RuntimeException("Household not found"));

        String token = jwtTokenProvider.generateToken(user.getId(), user.getEmail(), household.getId());

        return LoginResponse.builder()
                .token(token)
                .type("Bearer")
                .expiresIn(86400L) // 24 hours
                .user(UserResponse.fromUser(user, household.getId()))
                .build();
    }

    private void createDefaultCategories(Long householdId) {
        List<Category> categories = new ArrayList<>();
        
        // Expense categories
        categories.add(createCategory(householdId, "Food & Dining", Category.CategoryType.EXPENSE, "🍽️", "#FF6B6B"));
        categories.add(createCategory(householdId, "Transportation", Category.CategoryType.EXPENSE, "🚗", "#4ECDC4"));
        categories.add(createCategory(householdId, "Shopping", Category.CategoryType.EXPENSE, "🛍️", "#95E1D3"));
        categories.add(createCategory(householdId, "Entertainment", Category.CategoryType.EXPENSE, "🎬", "#F38181"));
        categories.add(createCategory(householdId, "Bills & Utilities", Category.CategoryType.EXPENSE, "📄", "#AA96DA"));
        categories.add(createCategory(householdId, "Healthcare", Category.CategoryType.EXPENSE, "🏥", "#FCBAD3"));
        categories.add(createCategory(householdId, "Education", Category.CategoryType.EXPENSE, "📚", "#FEC8D8"));
        categories.add(createCategory(householdId, "Travel", Category.CategoryType.EXPENSE, "✈️", "#7FCDCD"));
        categories.add(createCategory(householdId, "Housing", Category.CategoryType.EXPENSE, "🏠", "#FFAAA5"));
        categories.add(createCategory(householdId, "Other", Category.CategoryType.EXPENSE, "📦", "#B8B8B8"));
        
        // Income categories
        categories.add(createCategory(householdId, "Salary", Category.CategoryType.INCOME, "💰", "#51CF66"));
        categories.add(createCategory(householdId, "Business", Category.CategoryType.INCOME, "💼", "#94D82D"));
        categories.add(createCategory(householdId, "Investments", Category.CategoryType.INCOME, "📈", "#82C91E"));
        categories.add(createCategory(householdId, "Freelance", Category.CategoryType.INCOME, "💻", "#74C0FC"));
        categories.add(createCategory(householdId, "Other Income", Category.CategoryType.INCOME, "💵", "#91A7FF"));
        
        categoryRepository.saveAll(categories);
    }

    private Category createCategory(Long householdId, String name, Category.CategoryType type, String icon, String color) {
        return Category.builder()
                .householdId(householdId)
                .name(name)
                .type(type)
                .icon(icon)
                .color(color)
                .isDefault(true)
                .build();
    }
}
