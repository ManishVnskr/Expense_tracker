package com.expensetracker.service;

import com.expensetracker.dto.UserResponse;
import com.expensetracker.model.Household;
import com.expensetracker.model.User;
import com.expensetracker.repository.HouseholdRepository;
import com.expensetracker.repository.UserRepository;
import com.expensetracker.security.UserPrincipal;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final HouseholdRepository householdRepository;

    public UserService(UserRepository userRepository, HouseholdRepository householdRepository) {
        this.userRepository = userRepository;
        this.householdRepository = householdRepository;
    }

    public UserPrincipal getCurrentUserPrincipal() {
        return (UserPrincipal) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
    }

    public UserResponse getCurrentUser() {
        UserPrincipal principal = getCurrentUserPrincipal();
        User user = userRepository.findById(principal.getUserId())
                .orElseThrow(() -> new RuntimeException("User not found"));
        
        return UserResponse.fromUser(user, principal.getHouseholdId());
    }

    public void validateHouseholdAccess(Long householdId) {
        UserPrincipal principal = getCurrentUserPrincipal();
        if (!principal.getHouseholdId().equals(householdId)) {
            throw new RuntimeException("Access denied to this household");
        }
    }
}
