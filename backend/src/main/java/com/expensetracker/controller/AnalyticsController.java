package com.expensetracker.controller;

import com.expensetracker.dto.AnalyticsDto;
import com.expensetracker.service.AnalyticsService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/households/{householdId}/analytics")
public class AnalyticsController {

    private final AnalyticsService analyticsService;

    public AnalyticsController(AnalyticsService analyticsService) {
        this.analyticsService = analyticsService;
    }

    @GetMapping("/dashboard")
    public ResponseEntity<AnalyticsDto.DashboardResponse> getDashboard(@PathVariable Long householdId) {
        return ResponseEntity.ok(analyticsService.getDashboard(householdId));
    }

    @GetMapping("/trends")
    public ResponseEntity<AnalyticsDto.TrendsResponse> getTrends(
            @PathVariable Long householdId,
            @RequestParam(defaultValue = "6") int months) {
        return ResponseEntity.ok(analyticsService.getTrends(householdId, months));
    }
}
