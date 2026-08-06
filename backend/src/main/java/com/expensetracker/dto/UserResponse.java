package com.expensetracker.dto;

import com.expensetracker.model.User;
import lombok.Builder;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Builder
public class UserResponse {
    private Long id;
    private String email;
    private String fullName;
    private Long householdId;
    private LocalDateTime createdAt;
    
    public static UserResponse fromUser(User user, Long householdId) {
        return UserResponse.builder()
                .id(user.getId())
                .email(user.getEmail())
                .fullName(user.getFullName())
                .householdId(householdId)
                .createdAt(user.getCreatedAt())
                .build();
    }
}
