package com.expensetracker.dto;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class LoginResponse {
    private String token;
    private String type;
    private Long expiresIn;
    private UserResponse user;
}
