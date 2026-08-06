# Test Strategy Document

## Overview

Comprehensive testing strategy for the Expense Tracker application covering unit, integration, E2E, performance, and security testing.

**Testing Philosophy:** Test-driven development (TDD) where appropriate, with emphasis on critical business logic and user journeys.

---

## Testing Pyramid

```
           /\
          /  \
         / E2E \          10% - Critical user flows
        /--------\
       /          \
      / Integration \     30% - API contracts, DB queries
     /--------------\
    /                \
   /   Unit Tests     \   60% - Business logic, utilities
  /--------------------\
```

---

## Coverage Targets

| Test Type | Target Coverage | Tool |
|-----------|----------------|------|
| Unit Tests (Backend) | ≥ 80% | JUnit 5 + Jacoco |
| Unit Tests (Frontend) | ≥ 75% | Vitest |
| Integration Tests | ≥ 70% | Spring Boot Test + Testcontainers |
| E2E Tests | Critical paths (≥ 5 flows) | Playwright |
| API Contract Tests | 100% of endpoints | REST Assured / Pact |

---

## 1. Unit Testing

### 1.1 Backend Unit Tests (Java/Spring Boot)

**Framework:** JUnit 5 + Mockito + AssertJ

**What to Test:**
- Service layer business logic
- Utility functions
- Custom validators
- DTO mappings
- Enum operations

**Example: TransactionService Test**

```java
@ExtendWith(MockitoExtension.class)
class TransactionServiceTest {
    
    @Mock
    private TransactionRepository transactionRepository;
    
    @Mock
    private CategoryRepository categoryRepository;
    
    @Mock
    private RecurringPatternService recurringPatternService;
    
    @InjectMocks
    private TransactionService transactionService;
    
    @Test
    @DisplayName("Should create transaction successfully")
    void shouldCreateTransaction() {
        // Given
        TransactionRequest request = TransactionRequest.builder()
            .householdId(1L)
            .categoryId(1L)
            .amount(new BigDecimal("100.00"))
            .type(TransactionType.EXPENSE)
            .transactionDate(LocalDate.now())
            .build();
            
        Transaction savedTransaction = new Transaction();
        savedTransaction.setId(1L);
        
        when(categoryRepository.findById(1L))
            .thenReturn(Optional.of(new Category()));
        when(transactionRepository.save(any(Transaction.class)))
            .thenReturn(savedTransaction);
        
        // When
        TransactionResponse response = transactionService.createTransaction(request);
        
        // Then
        assertThat(response).isNotNull();
        assertThat(response.getId()).isEqualTo(1L);
        verify(recurringPatternService).detectPattern(any());
    }
    
    @Test
    @DisplayName("Should throw exception when category not found")
    void shouldThrowExceptionWhenCategoryNotFound() {
        // Given
        TransactionRequest request = TransactionRequest.builder()
            .categoryId(999L)
            .build();
            
        when(categoryRepository.findById(999L))
            .thenReturn(Optional.empty());
        
        // When & Then
        assertThatThrownBy(() -> transactionService.createTransaction(request))
            .isInstanceOf(ResourceNotFoundException.class)
            .hasMessage("Category not found with id: 999");
    }
    
    @Test
    @DisplayName("Should calculate monthly spending correctly")
    void shouldCalculateMonthlySpending() {
        // Given
        Long householdId = 1L;
        LocalDate startDate = LocalDate.of(2026, 8, 1);
        LocalDate endDate = LocalDate.of(2026, 8, 31);
        
        List<Transaction> transactions = Arrays.asList(
            createTransaction(new BigDecimal("100.00")),
            createTransaction(new BigDecimal("50.00")),
            createTransaction(new BigDecimal("75.50"))
        );
        
        when(transactionRepository.findByHouseholdIdAndDateRange(
            householdId, startDate, endDate))
            .thenReturn(transactions);
        
        // When
        BigDecimal total = transactionService.calculateTotalSpending(
            householdId, startDate, endDate);
        
        // Then
        assertThat(total).isEqualByComparingTo(new BigDecimal("225.50"));
    }
}
```

**Test Coverage Requirements:**
- ✓ Happy path scenarios
- ✓ Edge cases (empty lists, null values)
- ✓ Exception scenarios
- ✓ Boundary conditions (date ranges, amounts)
- ✓ Authorization checks

---

### 1.2 Frontend Unit Tests (React/TypeScript)

**Framework:** Vitest + React Testing Library

**What to Test:**
- Component rendering
- User interactions
- Custom hooks
- Utility functions
- Form validation logic

**Example: TransactionForm Test**

```typescript
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { TransactionForm } from './TransactionForm';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient({
  defaultOptions: { queries: { retry: false } }
});

const wrapper = ({ children }: { children: React.ReactNode }) => (
  <QueryClientProvider client={queryClient}>
    {children}
  </QueryClientProvider>
);

describe('TransactionForm', () => {
  it('should render all form fields', () => {
    render(<TransactionForm />, { wrapper });
    
    expect(screen.getByLabelText(/amount/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/category/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/description/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/date/i)).toBeInTheDocument();
  });
  
  it('should show validation errors for invalid input', async () => {
    render(<TransactionForm />, { wrapper });
    
    const submitButton = screen.getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);
    
    await waitFor(() => {
      expect(screen.getByText(/amount is required/i)).toBeInTheDocument();
      expect(screen.getByText(/category is required/i)).toBeInTheDocument();
    });
  });
  
  it('should call onSubmit with correct data', async () => {
    const mockOnSubmit = vi.fn();
    render(<TransactionForm onSubmit={mockOnSubmit} />, { wrapper });
    
    // Fill form
    fireEvent.change(screen.getByLabelText(/amount/i), {
      target: { value: '100.50' }
    });
    fireEvent.change(screen.getByLabelText(/description/i), {
      target: { value: 'Grocery shopping' }
    });
    
    // Submit
    const submitButton = screen.getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);
    
    await waitFor(() => {
      expect(mockOnSubmit).toHaveBeenCalledWith(
        expect.objectContaining({
          amount: 100.50,
          description: 'Grocery shopping'
        })
      );
    });
  });
  
  it('should disable submit button while loading', () => {
    render(<TransactionForm isLoading={true} />, { wrapper });
    
    const submitButton = screen.getByRole('button', { name: /submit/i });
    expect(submitButton).toBeDisabled();
  });
});
```

**Custom Hook Test Example:**

```typescript
import { describe, it, expect } from 'vitest';
import { renderHook, waitFor } from '@testing-library/react';
import { useTransactions } from './useTransactions';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

describe('useTransactions', () => {
  it('should fetch transactions successfully', async () => {
    const queryClient = new QueryClient();
    const wrapper = ({ children }: any) => (
      <QueryClientProvider client={queryClient}>
        {children}
      </QueryClientProvider>
    );
    
    const { result } = renderHook(
      () => useTransactions(1), 
      { wrapper }
    );
    
    await waitFor(() => expect(result.current.isSuccess).toBe(true));
    
    expect(result.current.data).toBeDefined();
    expect(Array.isArray(result.current.data)).toBe(true);
  });
});
```

---

## 2. Integration Testing

### 2.1 Backend Integration Tests

**Framework:** Spring Boot Test + Testcontainers + REST Assured

**What to Test:**
- API endpoints (Controller → Service → Repository)
- Database queries
- Transaction management
- Security filters
- Error handling

**Example: Transaction API Integration Test**

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
@Testcontainers
@ActiveProfiles("test")
class TransactionControllerIntegrationTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
        "postgres:15-alpine"
    );
    
    @LocalServerPort
    private int port;
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Autowired
    private TransactionRepository transactionRepository;
    
    private String jwtToken;
    
    @BeforeEach
    void setUp() {
        // Login and get JWT token
        LoginRequest loginRequest = new LoginRequest("test@example.com", "password");
        ResponseEntity<AuthResponse> response = restTemplate.postForEntity(
            "/api/v1/auth/login", 
            loginRequest, 
            AuthResponse.class
        );
        jwtToken = response.getBody().getToken();
    }
    
    @Test
    @DisplayName("POST /api/v1/households/{id}/transactions - Success")
    void shouldCreateTransaction() {
        // Given
        TransactionRequest request = TransactionRequest.builder()
            .categoryId(1L)
            .amount(new BigDecimal("100.00"))
            .type(TransactionType.EXPENSE)
            .description("Test transaction")
            .transactionDate(LocalDate.now())
            .build();
        
        HttpHeaders headers = new HttpHeaders();
        headers.setBearerAuth(jwtToken);
        HttpEntity<TransactionRequest> entity = new HttpEntity<>(request, headers);
        
        // When
        ResponseEntity<TransactionResponse> response = restTemplate.exchange(
            "/api/v1/households/1/transactions",
            HttpMethod.POST,
            entity,
            TransactionResponse.class
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody()).isNotNull();
        assertThat(response.getBody().getAmount())
            .isEqualByComparingTo(new BigDecimal("100.00"));
        
        // Verify database
        Transaction saved = transactionRepository.findById(
            response.getBody().getId()
        ).orElseThrow();
        assertThat(saved.getDescription()).isEqualTo("Test transaction");
    }
    
    @Test
    @DisplayName("GET /api/v1/households/{id}/transactions - With filters")
    void shouldGetTransactionsWithFilters() {
        // Given
        createTestTransactions();
        
        HttpHeaders headers = new HttpHeaders();
        headers.setBearerAuth(jwtToken);
        
        // When
        ResponseEntity<PageResponse<TransactionResponse>> response = restTemplate.exchange(
            "/api/v1/households/1/transactions?type=EXPENSE&startDate=2026-08-01",
            HttpMethod.GET,
            new HttpEntity<>(headers),
            new ParameterizedTypeReference<>() {}
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(response.getBody().getContent()).isNotEmpty();
        assertThat(response.getBody().getContent())
            .allMatch(t -> t.getType() == TransactionType.EXPENSE);
    }
    
    @Test
    @DisplayName("DELETE /api/v1/households/{id}/transactions/{tid} - Unauthorized")
    void shouldReturn403WhenUnauthorized() {
        // When - No JWT token
        ResponseEntity<String> response = restTemplate.exchange(
            "/api/v1/households/1/transactions/1",
            HttpMethod.DELETE,
            null,
            String.class
        );
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.UNAUTHORIZED);
    }
}
```

**Testcontainers Configuration:**

```java
@TestConfiguration
public class TestContainersConfig {
    
    @Bean
    @ServiceConnection
    public PostgreSQLContainer<?> postgresContainer() {
        return new PostgreSQLContainer<>("postgres:15-alpine")
            .withDatabaseName("expense_tracker_test")
            .withUsername("test")
            .withPassword("test");
    }
    
    @Bean
    @ServiceConnection
    public GenericContainer<?> redisContainer() {
        return new GenericContainer<>("redis:7-alpine")
            .withExposedPorts(6379);
    }
}
```

---

### 2.2 Frontend Integration Tests

**Framework:** Vitest + MSW (Mock Service Worker)

**What to Test:**
- Component + API integration
- TanStack Query caching behavior
- Error handling with real network delays

**Example: Dashboard Integration Test**

```typescript
import { describe, it, expect, beforeAll, afterAll, afterEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import { setupServer } from 'msw/node';
import { http, HttpResponse } from 'msw';
import { DashboardPage } from './DashboardPage';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const server = setupServer(
  http.get('/api/v1/households/:id/analytics/dashboard', () => {
    return HttpResponse.json({
      summary: {
        totalIncome: 5000.00,
        totalExpense: 3250.75,
        netAmount: 1749.25
      },
      topCategories: [
        { categoryName: 'Groceries', amount: 850.00 }
      ]
    });
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

describe('DashboardPage Integration', () => {
  it('should load and display dashboard data', async () => {
    const queryClient = new QueryClient();
    
    render(
      <QueryClientProvider client={queryClient}>
        <DashboardPage />
      </QueryClientProvider>
    );
    
    // Should show loading state
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
    
    // Should show data after loading
    await waitFor(() => {
      expect(screen.getByText(/\$5,000\.00/)).toBeInTheDocument();
      expect(screen.getByText(/\$3,250\.75/)).toBeInTheDocument();
      expect(screen.getByText(/Groceries/)).toBeInTheDocument();
    });
  });
  
  it('should handle API errors gracefully', async () => {
    server.use(
      http.get('/api/v1/households/:id/analytics/dashboard', () => {
        return HttpResponse.json(
          { error: 'Internal server error' },
          { status: 500 }
        );
      })
    );
    
    const queryClient = new QueryClient();
    
    render(
      <QueryClientProvider client={queryClient}>
        <DashboardPage />
      </QueryClientProvider>
    );
    
    await waitFor(() => {
      expect(screen.getByText(/error loading dashboard/i)).toBeInTheDocument();
    });
  });
});
```

---

## 3. Database Testing

### 3.1 Repository Tests

**Framework:** Spring Data JPA Test + Testcontainers

```java
@DataJpaTest
@AutoConfigureTestDatabase(replace = Replace.NONE)
@Testcontainers
class TransactionRepositoryTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
        "postgres:15-alpine"
    );
    
    @Autowired
    private TransactionRepository transactionRepository;
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Test
    @DisplayName("Should find transactions by date range")
    void shouldFindByDateRange() {
        // Given
        LocalDate startDate = LocalDate.of(2026, 8, 1);
        LocalDate endDate = LocalDate.of(2026, 8, 31);
        
        Transaction tx1 = createTransaction(LocalDate.of(2026, 8, 5));
        Transaction tx2 = createTransaction(LocalDate.of(2026, 8, 15));
        Transaction tx3 = createTransaction(LocalDate.of(2026, 9, 1)); // Outside range
        
        entityManager.persist(tx1);
        entityManager.persist(tx2);
        entityManager.persist(tx3);
        entityManager.flush();
        
        // When
        List<Transaction> result = transactionRepository
            .findByHouseholdIdAndDateRange(1L, startDate, endDate);
        
        // Then
        assertThat(result).hasSize(2);
        assertThat(result).extracting(Transaction::getId)
            .containsExactlyInAnyOrder(tx1.getId(), tx2.getId());
    }
    
    @Test
    @DisplayName("Should calculate sum by category")
    void shouldCalculateSumByCategory() {
        // Given
        createTransactionWithCategory(1L, new BigDecimal("100.00"));
        createTransactionWithCategory(1L, new BigDecimal("50.00"));
        createTransactionWithCategory(2L, new BigDecimal("200.00"));
        
        // When
        BigDecimal sum = transactionRepository
            .sumAmountByCategoryId(1L);
        
        // Then
        assertThat(sum).isEqualByComparingTo(new BigDecimal("150.00"));
    }
}
```

---

**[Continued in next section...]**

## 4. End-to-End (E2E) Testing

### 4.1 Critical User Journeys

**Framework:** Playwright

**Priority E2E Tests:**

1. **User Registration & Login Flow**
2. **Create Transaction & View in Dashboard**
3. **Create Budget & Receive Alert**
4. **Multi-user Household Sharing**
5. **Export Transactions to CSV**

**Example: Complete Transaction Flow**

```typescript
// e2e/transaction-flow.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Transaction Management Flow', () => {
  test.beforeEach(async ({ page }) => {
    // Login
    await page.goto('/login');
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'password123');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
  });
  
  test('should create, edit, and delete a transaction', async ({ page }) => {
    // Navigate to transactions page
    await page.click('text=Transactions');
    await expect(page).toHaveURL(/.*transactions/);
    
    // Click "Add Transaction" button
    await page.click('button:has-text("Add Transaction")');
    
    // Fill transaction form
    await page.fill('[name="amount"]', '125.50');
    await page.selectOption('[name="category"]', 'Groceries');
    await page.fill('[name="description"]', 'Weekly grocery shopping');
    await page.fill('[name="transactionDate"]', '2026-08-03');
    await page.selectOption('[name="paymentMethod"]', 'CARD');
    
    // Submit form
    await page.click('button:has-text("Create Transaction")');
    
    // Verify success toast
    await expect(page.locator('.toast-success')).toContainText(
      'Transaction created successfully'
    );
    
    // Verify transaction appears in list
    await expect(page.locator('table')).toContainText('Weekly grocery shopping');
    await expect(page.locator('table')).toContainText('$125.50');
    
    // Edit transaction
    await page.click('tr:has-text("Weekly grocery shopping") button[aria-label="Edit"]');
    await page.fill('[name="amount"]', '130.00');
    await page.click('button:has-text("Update")');
    
    // Verify update
    await expect(page.locator('table')).toContainText('$130.00');
    
    // Delete transaction
    await page.click('tr:has-text("Weekly grocery shopping") button[aria-label="Delete"]');
    await page.click('button:has-text("Confirm")');
    
    // Verify deletion
    await expect(page.locator('table')).not.toContainText('Weekly grocery shopping');
  });
  
  test('should filter transactions by date range', async ({ page }) => {
    await page.goto('/transactions');
    
    // Open filter panel
    await page.click('button:has-text("Filters")');
    
    // Set date range
    await page.fill('[name="startDate"]', '2026-08-01');
    await page.fill('[name="endDate"]', '2026-08-31');
    await page.click('button:has-text("Apply Filters")');
    
    // Wait for filtered results
    await page.waitForLoadState('networkidle');
    
    // Verify all transactions are within range
    const dates = await page.locator('table tbody tr td:nth-child(2)').allTextContents();
    for (const date of dates) {
      const txDate = new Date(date);
      expect(txDate >= new Date('2026-08-01')).toBeTruthy();
      expect(txDate <= new Date('2026-08-31')).toBeTruthy();
    }
  });
  
  test('should export transactions to CSV', async ({ page }) => {
    await page.goto('/transactions');
    
    // Click export button
    const downloadPromise = page.waitForEvent('download');
    await page.click('button:has-text("Export CSV")');
    const download = await downloadPromise;
    
    // Verify filename
    expect(download.suggestedFilename()).toMatch(/transactions_\d{8}\.csv/);
    
    // Verify file content
    const path = await download.path();
    const fs = require('fs');
    const content = fs.readFileSync(path, 'utf-8');
    expect(content).toContain('Date,Category,Amount,Description');
  });
});
```

**Budget Alert E2E Test:**

```typescript
test('should receive budget alert when threshold exceeded', async ({ page }) => {
  // Create budget with 80% alert threshold
  await page.goto('/budgets');
  await page.click('button:has-text("Create Budget")');
  await page.fill('[name="name"]', 'August Groceries');
  await page.fill('[name="amount"]', '500.00');
  await page.selectOption('[name="category"]', 'Groceries');
  await page.fill('[name="alertThreshold"]', '80');
  await page.click('button:has-text("Create")');
  
  // Create transaction that exceeds 80%
  await page.goto('/transactions');
  await page.click('button:has-text("Add Transaction")');
  await page.fill('[name="amount"]', '410.00'); // 82% of budget
  await page.selectOption('[name="category"]', 'Groceries');
  await page.click('button:has-text("Create")');
  
  // Verify alert notification appears
  await expect(page.locator('.alert-warning')).toContainText(
    'August Groceries budget is at 82%'
  );
  
  // Verify budget card shows warning state
  await page.goto('/budgets');
  const budgetCard = page.locator('.budget-card:has-text("August Groceries")');
  await expect(budgetCard).toHaveClass(/warning/);
});
```

---

### 4.2 Multi-User Scenarios

```typescript
test.describe('Household Sharing', () => {
  test('should allow owner to invite member and member to view transactions', async ({ browser }) => {
    // Context 1: Owner
    const ownerContext = await browser.newContext();
    const ownerPage = await ownerContext.newPage();
    await ownerPage.goto('/login');
    await loginAs(ownerPage, 'owner@example.com', 'password');
    
    // Owner invites member
    await ownerPage.goto('/households/1/settings');
    await ownerPage.click('button:has-text("Invite Member")');
    await ownerPage.fill('[name="email"]', 'member@example.com');
    await ownerPage.selectOption('[name="role"]', 'VIEWER');
    await ownerPage.click('button:has-text("Send Invitation")');
    
    // Get invitation link from page
    const inviteLink = await ownerPage.locator('.invite-link').textContent();
    
    // Context 2: New member
    const memberContext = await browser.newContext();
    const memberPage = await memberContext.newPage();
    await memberPage.goto(inviteLink);
    await memberPage.click('button:has-text("Accept Invitation")');
    
    // Member logs in
    await loginAs(memberPage, 'member@example.com', 'password');
    
    // Member can view transactions
    await memberPage.goto('/transactions');
    await expect(memberPage.locator('table')).toBeVisible();
    
    // Member cannot create transactions (VIEWER role)
    await expect(memberPage.locator('button:has-text("Add Transaction")')).toBeDisabled();
    
    // Cleanup
    await ownerContext.close();
    await memberContext.close();
  });
});
```

---

### 4.3 E2E Test Configuration

**playwright.config.ts**

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html'],
    ['junit', { outputFile: 'test-results/junit.xml' }]
  ],
  use: {
    baseURL: 'http://localhost:5173',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'mobile',
      use: { ...devices['iPhone 13'] },
    },
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:5173',
    reuseExistingServer: !process.env.CI,
  },
});
```

---

## 5. Performance Testing

### 5.1 Backend Load Testing

**Tool:** k6

**Scenarios to Test:**
1. Transaction creation under load
2. Dashboard analytics query performance
3. Concurrent user sessions
4. Database connection pool behavior

**Example: Transaction Creation Load Test**

```javascript
// k6-load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

export const errorRate = new Rate('errors');

export const options = {
  stages: [
    { duration: '2m', target: 50 },  // Ramp up to 50 users
    { duration: '5m', target: 50 },  // Stay at 50 users
    { duration: '2m', target: 100 }, // Ramp up to 100 users
    { duration: '5m', target: 100 }, // Stay at 100 users
    { duration: '2m', target: 0 },   // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests under 500ms
    errors: ['rate<0.1'],              // Error rate < 10%
  },
};

const BASE_URL = 'http://localhost:8080/api/v1';
let authToken;

export function setup() {
  // Login to get JWT token
  const loginRes = http.post(`${BASE_URL}/auth/login`, JSON.stringify({
    email: 'loadtest@example.com',
    password: 'password123'
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
  
  return { token: loginRes.json('token') };
}

export default function(data) {
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${data.token}`,
    },
  };
  
  // Create transaction
  const payload = JSON.stringify({
    householdId: 1,
    categoryId: 1,
    amount: Math.random() * 1000,
    type: 'EXPENSE',
    description: 'Load test transaction',
    transactionDate: '2026-08-03',
  });
  
  const createRes = http.post(
    `${BASE_URL}/households/1/transactions`,
    payload,
    params
  );
  
  check(createRes, {
    'status is 201': (r) => r.status === 201,
    'response time < 500ms': (r) => r.timings.duration < 500,
  }) || errorRate.add(1);
  
  sleep(1);
  
  // Fetch transactions
  const getRes = http.get(
    `${BASE_URL}/households/1/transactions?page=0&size=20`,
    params
  );
  
  check(getRes, {
    'status is 200': (r) => r.status === 200,
    'has transactions': (r) => r.json('content').length > 0,
  });
  
  sleep(2);
}
```

**Run Load Test:**
```bash
k6 run k6-load-test.js
```

---

### 5.2 Database Performance Testing

**Query Performance Benchmarks:**

| Query | Expected Time | Max Acceptable |
|-------|---------------|----------------|
| Fetch 50 transactions | < 50ms | 100ms |
| Dashboard analytics (1 month) | < 200ms | 500ms |
| Budget calculation | < 100ms | 300ms |
| Category breakdown | < 150ms | 400ms |

**JMH Benchmark Example:**

```java
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Benchmark)
public class TransactionQueryBenchmark {
    
    @Autowired
    private TransactionRepository transactionRepository;
    
    @Benchmark
    public void fetchLast50Transactions() {
        transactionRepository.findTop50ByHouseholdIdOrderByTransactionDateDesc(1L);
    }
    
    @Benchmark
    public void calculateMonthlySpending() {
        LocalDate start = LocalDate.of(2026, 8, 1);
        LocalDate end = LocalDate.of(2026, 8, 31);
        transactionRepository.sumAmountByHouseholdIdAndDateRange(1L, start, end);
    }
}
```

---

### 5.3 Frontend Performance Testing

**Tool:** Lighthouse CI

**Metrics Targets:**

| Metric | Target | Minimum |
|--------|--------|---------|
| Performance Score | ≥ 90 | 80 |
| First Contentful Paint | < 1.5s | 2.5s |
| Largest Contentful Paint | < 2.5s | 4.0s |
| Time to Interactive | < 3.5s | 5.5s |
| Cumulative Layout Shift | < 0.1 | 0.25 |

**Lighthouse CI Configuration:**

```javascript
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      startServerCommand: 'npm run preview',
      url: ['http://localhost:4173/'],
      numberOfRuns: 3,
    },
    assert: {
      preset: 'lighthouse:recommended',
      assertions: {
        'categories:performance': ['error', { minScore: 0.9 }],
        'categories:accessibility': ['error', { minScore: 0.95 }],
        'first-contentful-paint': ['error', { maxNumericValue: 1500 }],
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
};
```

---

## 6. Security Testing

### 6.1 OWASP Top 10 Checklist

| Vulnerability | Test Method | Status |
|---------------|-------------|--------|
| **A01: Broken Access Control** | Manual + Automated | ✓ |
| **A02: Cryptographic Failures** | Code Review | ✓ |
| **A03: Injection (SQL, XSS)** | SAST + Manual | ✓ |
| **A04: Insecure Design** | Architecture Review | ✓ |
| **A05: Security Misconfiguration** | Config Audit | ✓ |
| **A06: Vulnerable Components** | Dependency Scan | ✓ |
| **A07: Auth/Session Failures** | Manual Testing | ✓ |
| **A08: Data Integrity Failures** | Manual Testing | ✓ |
| **A09: Logging Failures** | Code Review | ✓ |
| **A10: SSRF** | Manual Testing | ✓ |

---

### 6.2 JWT Security Tests

```java
@SpringBootTest
class JwtSecurityTest {
    
    @Test
    void shouldRejectExpiredToken() {
        String expiredToken = generateExpiredToken();
        
        given()
            .header("Authorization", "Bearer " + expiredToken)
        .when()
            .get("/api/v1/transactions")
        .then()
            .statusCode(401)
            .body("error", equalTo("UNAUTHORIZED"));
    }
    
    @Test
    void shouldRejectTamperedToken() {
        String validToken = generateValidToken();
        String tamperedToken = validToken.substring(0, validToken.length() - 10) + "TAMPERED";
        
        given()
            .header("Authorization", "Bearer " + tamperedToken)
        .when()
            .get("/api/v1/transactions")
        .then()
            .statusCode(401);
    }
    
    @Test
    void shouldRejectTokenWithInvalidSignature() {
        String tokenWithWrongSecret = Jwts.builder()
            .setSubject("test@example.com")
            .signWith(Keys.hmacShaKeyFor("wrong-secret-key".getBytes()))
            .compact();
        
        given()
            .header("Authorization", "Bearer " + tokenWithWrongSecret)
        .when()
            .get("/api/v1/transactions")
        .then()
            .statusCode(401);
    }
}
```

---

### 6.3 Authorization Tests

```java
@Test
void shouldPreventViewerFromCreatingTransaction() {
    // Login as VIEWER role user
    String viewerToken = loginAs("viewer@example.com");
    
    TransactionRequest request = new TransactionRequest();
    request.setAmount(new BigDecimal("100.00"));
    
    given()
        .header("Authorization", "Bearer " + viewerToken)
        .contentType(ContentType.JSON)
        .body(request)
    .when()
        .post("/api/v1/households/1/transactions")
    .then()
        .statusCode(403)
        .body("error", equalTo("FORBIDDEN"));
}

@Test
void shouldPreventAccessToOtherHouseholdData() {
    String user1Token = loginAs("user1@example.com"); // Member of household 1
    
    given()
        .header("Authorization", "Bearer " + user1Token)
    .when()
        .get("/api/v1/households/2/transactions") // Household 2
    .then()
        .statusCode(403);
}
```

---

### 6.4 SQL Injection Prevention

```java
@Test
void shouldPreventSqlInjectionInSearch() {
    String maliciousQuery = "'; DROP TABLE transactions; --";
    
    given()
        .header("Authorization", "Bearer " + validToken)
        .queryParam("search", maliciousQuery)
    .when()
        .get("/api/v1/households/1/transactions")
    .then()
        .statusCode(200); // Should return empty results, not execute SQL
    
    // Verify table still exists
    List<Transaction> transactions = transactionRepository.findAll();
    assertThat(transactions).isNotNull(); // Table not dropped
}
```

---

### 6.5 XSS Prevention Tests

```typescript
test('should sanitize user input to prevent XSS', async ({ page }) => {
  await page.goto('/transactions');
  await page.click('button:has-text("Add Transaction")');
  
  const xssPayload = '<script>alert("XSS")</script>';
  await page.fill('[name="description"]', xssPayload);
  await page.click('button:has-text("Create")');
  
  // Wait for transaction to appear
  await page.waitForSelector('table');
  
  // Verify script is escaped, not executed
  const description = await page.locator('table').textContent();
  expect(description).toContain('&lt;script&gt;');
  
  // Verify no alert dialog appeared
  page.on('dialog', () => {
    throw new Error('XSS vulnerability detected: alert executed');
  });
});
```

---

### 6.6 Dependency Scanning

**Tools:**
- **Backend:** OWASP Dependency-Check, Snyk
- **Frontend:** npm audit, Snyk

**Maven Configuration:**

```xml
<plugin>
    <groupId>org.owasp</groupId>
    <artifactId>dependency-check-maven</artifactId>
    <version>8.4.0</version>
    <executions>
        <execution>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
    <configuration>
        <failBuildOnCVSS>7</failBuildOnCVSS>
    </configuration>
</plugin>
```

**Run Scan:**
```bash
# Backend
mvn dependency-check:check

# Frontend
npm audit --audit-level=moderate
```

---

## 7. Test Data Management

### 7.1 Test Data Builder Pattern

```java
public class TransactionTestDataBuilder {
    private Transaction transaction = new Transaction();
    
    public TransactionTestDataBuilder() {
        // Set sensible defaults
        transaction.setAmount(new BigDecimal("100.00"));
        transaction.setType(TransactionType.EXPENSE);
        transaction.setTransactionDate(LocalDate.now());
        transaction.setDescription("Test transaction");
    }
    
    public TransactionTestDataBuilder withAmount(BigDecimal amount) {
        transaction.setAmount(amount);
        return this;
    }
    
    public TransactionTestDataBuilder withCategory(Category category) {
        transaction.setCategory(category);
        return this;
    }
    
    public TransactionTestDataBuilder withDate(LocalDate date) {
        transaction.setTransactionDate(date);
        return this;
    }
    
    public Transaction build() {
        return transaction;
    }
}

// Usage in tests
Transaction tx = new TransactionTestDataBuilder()
    .withAmount(new BigDecimal("250.00"))
    .withDate(LocalDate.of(2026, 8, 1))
    .build();
```

---

### 7.2 Database Seeding for E2E Tests

```sql
-- test-data.sql
-- Run before E2E tests

-- Users
INSERT INTO users (email, password_hash, full_name, role) VALUES
('owner@example.com', '$2a$10$...', 'Test Owner', 'USER'),
('admin@example.com', '$2a$10$...', 'Test Admin', 'USER'),
('viewer@example.com', '$2a$10$...', 'Test Viewer', 'USER');

-- Household
INSERT INTO households (name, currency) VALUES ('Test Household', 'USD');

-- User-Household relationships
INSERT INTO user_households (user_id, household_id, role) VALUES
(1, 1, 'OWNER'),
(2, 1, 'ADMIN'),
(3, 1, 'VIEWER');

-- Categories
INSERT INTO categories (household_id, name, type, icon, color) VALUES
(1, 'Groceries', 'EXPENSE', 'shopping-cart', '#22c55e'),
(1, 'Salary', 'INCOME', 'dollar-sign', '#10b981');

-- Sample transactions
INSERT INTO transactions (household_id, user_id, category_id, amount, type, description, transaction_date) VALUES
(1, 1, 1, 100.00, 'EXPENSE', 'Walmart groceries', '2026-08-01'),
(1, 1, 1, 75.50, 'EXPENSE', 'Target shopping', '2026-08-05'),
(1, 1, 2, 5000.00, 'INCOME', 'Monthly salary', '2026-08-01');
```

---

## 8. Continuous Integration Testing

### 8.1 GitHub Actions Workflow

```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15-alpine
        env:
          POSTGRES_DB: expense_tracker_test
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      
      - name: Cache Maven packages
        uses: actions/cache@v3
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
      
      - name: Run Unit Tests
        run: mvn test
      
      - name: Run Integration Tests
        run: mvn verify -Pintegration-test
      
      - name: Generate Coverage Report
        run: mvn jacoco:report
      
      - name: Upload Coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./target/site/jacoco/jacoco.xml
      
      - name: Check Coverage Threshold
        run: |
          mvn jacoco:check -Djacoco.minimum-coverage=0.80

  frontend-tests:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run Linter
        run: npm run lint
      
      - name: Run Type Check
        run: npm run type-check
      
      - name: Run Unit Tests
        run: npm run test:unit -- --coverage
      
      - name: Upload Coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json

  e2e-tests:
    runs-on: ubuntu-latest
    needs: [backend-tests, frontend-tests]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright
        run: npx playwright install --with-deps
      
      - name: Start Backend
        run: |
          cd backend
          mvn spring-boot:run &
          sleep 30
      
      - name: Run E2E Tests
        run: npm run test:e2e
      
      - name: Upload Playwright Report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: playwright-report/

  security-scan:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Snyk Security Scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      
      - name: Run OWASP Dependency Check
        run: mvn dependency-check:check
```

---

## 9. Test Reporting & Monitoring

### 9.1 Coverage Reports

**JaCoCo Configuration (Backend):**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.10</version>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
        <execution>
            <id>check</id>
            <goals>
                <goal>check</goal>
            </goals>
            <configuration>
                <rules>
                    <rule>
                        <element>PACKAGE</element>
                        <limits>
                            <limit>
                                <counter>LINE</counter>
                                <value>COVEREDRATIO</value>
                                <minimum>0.80</minimum>
                            </limit>
                        </limits>
                    </rule>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>
```

---

## 10. Definition of Done (DoD)

A feature is considered **DONE** when:

- [ ] **Unit Tests:** All new code has unit tests with ≥ 80% coverage
- [ ] **Integration Tests:** API endpoints have integration tests
- [ ] **E2E Tests:** Critical paths have E2E test coverage (if applicable)
- [ ] **Manual Testing:** Feature tested manually in dev environment
- [ ] **Code Review:** At least one approval from team member
- [ ] **Security Review:** No new vulnerabilities introduced (Snyk scan passes)
- [ ] **Performance:** No performance regression (load test passes)
- [ ] **Documentation:** API docs and README updated
- [ ] **Accessibility:** WCAG 2.1 AA compliance verified
- [ ] **Cross-browser:** Tested in Chrome, Firefox, Safari (for frontend)
- [ ] **CI/CD:** All pipeline checks pass

---

**Document Version:** 1.0  
**Last Updated:** August 4, 2026  
**Owner:** QA Team
