# Architecture Diagrams

## Overview

This document provides comprehensive architecture diagrams for the Expense Tracker application using C4 model and component diagrams.

---

## 1. System Context Diagram (C4 Level 1)

```mermaid
graph TB
    User[User<br/>Web Browser]
    Admin[Admin User<br/>Web Browser]
    
    ExpenseTracker[Expense Tracker System<br/>Full-stack expense management]
    
    EmailService[Email Service<br/>SMTP]
    BlobStorage[File Storage<br/>AWS S3 / Local]
    
    User -->|Manages expenses,<br/>views analytics| ExpenseTracker
    Admin -->|Manages households,<br/>configures system| ExpenseTracker
    
    ExpenseTracker -->|Sends notifications,<br/>invitations| EmailService
    ExpenseTracker -->|Stores exported<br/>reports, receipts| BlobStorage
    
    style ExpenseTracker fill:#1168bd,stroke:#0b4884,color:#ffffff
    style User fill:#08427b,stroke:#052e56,color:#ffffff
    style Admin fill:#08427b,stroke:#052e56,color:#ffffff
```

---

## 2. Container Diagram (C4 Level 2)

```mermaid
graph TB
    User[User<br/>Web Browser]
    
    subgraph "Expense Tracker System"
        WebApp[Web Application<br/>React + TypeScript<br/>Port: 5173]
        API[API Application<br/>Spring Boot<br/>Port: 8080]
        DB[(PostgreSQL Database<br/>Port: 5432)]
        Cache[(Redis Cache<br/>Session & Query Cache<br/>Port: 6379)]
    end
    
    EmailService[Email Service<br/>SMTP]
    BlobStorage[File Storage<br/>AWS S3]
    
    User -->|HTTPS| WebApp
    WebApp -->|REST API<br/>JSON/HTTPS| API
    API -->|JDBC<br/>SQL Queries| DB
    API -->|Cache queries| Cache
    API -->|Send emails| EmailService
    API -->|Upload/Download<br/>files| BlobStorage
    
    style WebApp fill:#438dd5,stroke:#2e6295,color:#ffffff
    style API fill:#438dd5,stroke:#2e6295,color:#ffffff
    style DB fill:#1168bd,stroke:#0b4884,color:#ffffff
    style Cache fill:#1168bd,stroke:#0b4884,color:#ffffff
```

---

## 3. Component Diagram - Backend (C4 Level 3)

```mermaid
graph TB
    subgraph "API Application - Spring Boot"
        SecurityFilter[Security Filter<br/>JWT Validation]
        
        subgraph "Controllers"
            AuthController[Auth Controller]
            UserController[User Controller]
            HouseholdController[Household Controller]
            TransactionController[Transaction Controller]
            BudgetController[Budget Controller]
            AnalyticsController[Analytics Controller]
        end
        
        subgraph "Services"
            AuthService[Auth Service]
            UserService[User Service]
            HouseholdService[Household Service]
            TransactionService[Transaction Service]
            BudgetService[Budget Service]
            AnalyticsService[Analytics Service]
            RecurringPatternService[Recurring Pattern Service]
        end
        
        subgraph "Repositories"
            UserRepo[User Repository]
            HouseholdRepo[Household Repository]
            TransactionRepo[Transaction Repository]
            BudgetRepo[Budget Repository]
            CategoryRepo[Category Repository]
        end
        
        subgraph "External Services"
            EmailService[Email Service]
            StorageService[Storage Service]
            PDFGenerator[PDF Generator]
        end
    end
    
    WebApp[Web Application] -->|REST Calls| SecurityFilter
    SecurityFilter --> AuthController
    SecurityFilter --> UserController
    SecurityFilter --> HouseholdController
    SecurityFilter --> TransactionController
    SecurityFilter --> BudgetController
    SecurityFilter --> AnalyticsController
    
    AuthController --> AuthService
    UserController --> UserService
    HouseholdController --> HouseholdService
    TransactionController --> TransactionService
    BudgetController --> BudgetService
    AnalyticsController --> AnalyticsService
    
    TransactionService --> RecurringPatternService
    
    AuthService --> UserRepo
    UserService --> UserRepo
    HouseholdService --> HouseholdRepo
    TransactionService --> TransactionRepo
    BudgetService --> BudgetRepo
    TransactionService --> CategoryRepo
    
    AuthService --> EmailService
    AnalyticsService --> PDFGenerator
    TransactionService --> StorageService
    
    UserRepo --> DB[(Database)]
    HouseholdRepo --> DB
    TransactionRepo --> DB
    BudgetRepo --> DB
    CategoryRepo --> DB
    
    style SecurityFilter fill:#ff6b6b,stroke:#c92a2a,color:#ffffff
```

---

## 4. Component Diagram - Frontend (React)

```mermaid
graph TB
    subgraph "Frontend Application - React"
        subgraph "Pages"
            LoginPage[Login Page]
            DashboardPage[Dashboard Page]
            TransactionsPage[Transactions Page]
            BudgetsPage[Budgets Page]
            AnalyticsPage[Analytics Page]
            SettingsPage[Settings Page]
        end
        
        subgraph "Feature Components"
            TransactionList[Transaction List]
            TransactionForm[Transaction Form]
            BudgetCard[Budget Card]
            CategorySelector[Category Selector]
            DateRangePicker[Date Range Picker]
            ChartComponents[Chart Components]
        end
        
        subgraph "Shared Components (shadcn/ui)"
            Button[Button]
            Input[Input]
            Dialog[Dialog]
            Table[Table]
            Card[Card]
        end
        
        subgraph "State Management"
            AuthContext[Auth Context]
            HouseholdContext[Household Context]
            QueryClient[TanStack Query Client]
        end
        
        subgraph "API Layer"
            AuthAPI[Auth API]
            TransactionAPI[Transaction API]
            BudgetAPI[Budget API]
            AnalyticsAPI[Analytics API]
        end
        
        Router[React Router] --> LoginPage
        Router --> DashboardPage
        Router --> TransactionsPage
        Router --> BudgetsPage
        Router --> AnalyticsPage
        Router --> SettingsPage
        
        DashboardPage --> ChartComponents
        TransactionsPage --> TransactionList
        TransactionsPage --> TransactionForm
        BudgetsPage --> BudgetCard
        
        TransactionList --> Table
        TransactionForm --> Input
        TransactionForm --> Button
        TransactionForm --> CategorySelector
        BudgetCard --> Card
        
        TransactionList --> QueryClient
        TransactionForm --> QueryClient
        BudgetCard --> QueryClient
        
        QueryClient --> AuthAPI
        QueryClient --> TransactionAPI
        QueryClient --> BudgetAPI
        QueryClient --> AnalyticsAPI
        
        AuthAPI -->|REST| Backend[Backend API]
        TransactionAPI -->|REST| Backend
        BudgetAPI -->|REST| Backend
        AnalyticsAPI -->|REST| Backend
        
        AuthContext -.->|Provides| LoginPage
        HouseholdContext -.->|Provides| DashboardPage
    end
    
    style Router fill:#61dafb,stroke:#21a1c4,color:#000000
    style QueryClient fill:#ff4154,stroke:#c91f2e,color:#ffffff
```

---

## 5. Frontend Folder Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ui/                    # shadcn/ui components
│   │   │   ├── button.tsx
│   │   │   ├── input.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── table.tsx
│   │   │   └── card.tsx
│   │   ├── layout/
│   │   │   ├── AppLayout.tsx      # Main app layout with sidebar
│   │   │   ├── Navbar.tsx
│   │   │   └── Sidebar.tsx
│   │   ├── transactions/
│   │   │   ├── TransactionList.tsx
│   │   │   ├── TransactionForm.tsx
│   │   │   ├── TransactionFilters.tsx
│   │   │   └── TransactionCard.tsx
│   │   ├── budgets/
│   │   │   ├── BudgetCard.tsx
│   │   │   ├── BudgetForm.tsx
│   │   │   ├── BudgetProgress.tsx
│   │   │   └── BudgetAlerts.tsx
│   │   ├── analytics/
│   │   │   ├── SpendingChart.tsx
│   │   │   ├── CategoryPieChart.tsx
│   │   │   ├── TrendLineChart.tsx
│   │   │   └── DashboardCard.tsx
│   │   ├── categories/
│   │   │   ├── CategorySelector.tsx
│   │   │   ├── CategoryManager.tsx
│   │   │   └── CategoryIcon.tsx
│   │   └── shared/
│   │       ├── DateRangePicker.tsx
│   │       ├── CurrencyInput.tsx
│   │       ├── LoadingSpinner.tsx
│   │       └── ErrorBoundary.tsx
│   ├── pages/
│   │   ├── auth/
│   │   │   ├── LoginPage.tsx
│   │   │   └── RegisterPage.tsx
│   │   ├── DashboardPage.tsx
│   │   ├── TransactionsPage.tsx
│   │   ├── BudgetsPage.tsx
│   │   ├── AnalyticsPage.tsx
│   │   ├── CategoriesPage.tsx
│   │   ├── HouseholdsPage.tsx
│   │   └── SettingsPage.tsx
│   ├── api/
│   │   ├── client.ts              # Axios instance with interceptors
│   │   ├── auth.api.ts
│   │   ├── transactions.api.ts
│   │   ├── budgets.api.ts
│   │   ├── categories.api.ts
│   │   ├── households.api.ts
│   │   └── analytics.api.ts
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   ├── useTransactions.ts     # TanStack Query hooks
│   │   ├── useBudgets.ts
│   │   ├── useCategories.ts
│   │   └── useHouseholds.ts
│   ├── contexts/
│   │   ├── AuthContext.tsx
│   │   └── HouseholdContext.tsx
│   ├── types/
│   │   ├── auth.types.ts
│   │   ├── transaction.types.ts
│   │   ├── budget.types.ts
│   │   └── api.types.ts
│   ├── utils/
│   │   ├── formatters.ts          # Currency, date formatting
│   │   ├── validators.ts
│   │   └── constants.ts
│   ├── lib/
│   │   └── utils.ts               # shadcn/ui utility functions
│   ├── App.tsx
│   ├── main.tsx
│   └── routes.tsx
├── public/
├── package.json
├── vite.config.ts
├── tailwind.config.js
└── tsconfig.json
```

---

## 6. Backend Folder Structure

```
backend/
├── src/main/java/com/expensetracker/
│   ├── ExpenseTrackerApplication.java
│   ├── config/
│   │   ├── SecurityConfig.java        # Spring Security configuration
│   │   ├── JwtConfig.java
│   │   ├── CorsConfig.java
│   │   ├── OpenApiConfig.java         # Swagger configuration
│   │   └── CacheConfig.java
│   ├── security/
│   │   ├── JwtTokenProvider.java
│   │   ├── JwtAuthenticationFilter.java
│   │   ├── UserDetailsServiceImpl.java
│   │   └── SecurityUtils.java
│   ├── controller/
│   │   ├── AuthController.java
│   │   ├── UserController.java
│   │   ├── HouseholdController.java
│   │   ├── CategoryController.java
│   │   ├── TransactionController.java
│   │   ├── BudgetController.java
│   │   ├── AnalyticsController.java
│   │   └── ExportController.java
│   ├── service/
│   │   ├── AuthService.java
│   │   ├── UserService.java
│   │   ├── HouseholdService.java
│   │   ├── CategoryService.java
│   │   ├── TransactionService.java
│   │   ├── BudgetService.java
│   │   ├── AnalyticsService.java
│   │   ├── RecurringPatternService.java
│   │   ├── EmailService.java
│   │   ├── StorageService.java
│   │   └── PdfGeneratorService.java
│   ├── repository/
│   │   ├── UserRepository.java
│   │   ├── HouseholdRepository.java
│   │   ├── UserHouseholdRepository.java
│   │   ├── CategoryRepository.java
│   │   ├── TransactionRepository.java
│   │   ├── BudgetRepository.java
│   │   ├── BudgetCategoryRepository.java
│   │   └── RecurringPatternRepository.java
│   ├── model/
│   │   ├── entity/
│   │   │   ├── User.java
│   │   │   ├── Household.java
│   │   │   ├── UserHousehold.java
│   │   │   ├── Category.java
│   │   │   ├── Transaction.java
│   │   │   ├── Budget.java
│   │   │   ├── BudgetCategory.java
│   │   │   └── RecurringPattern.java
│   │   └── enums/
│   │       ├── Role.java
│   │       ├── TransactionType.java
│   │       ├── PeriodType.java
│   │       └── Frequency.java
│   ├── dto/
│   │   ├── request/
│   │   │   ├── LoginRequest.java
│   │   │   ├── RegisterRequest.java
│   │   │   ├── TransactionRequest.java
│   │   │   ├── BudgetRequest.java
│   │   │   └── CategoryRequest.java
│   │   └── response/
│   │       ├── AuthResponse.java
│   │       ├── TransactionResponse.java
│   │       ├── BudgetResponse.java
│   │       ├── AnalyticsResponse.java
│   │       └── PageResponse.java
│   ├── exception/
│   │   ├── GlobalExceptionHandler.java
│   │   ├── ResourceNotFoundException.java
│   │   ├── UnauthorizedException.java
│   │   └── ValidationException.java
│   └── util/
│       ├── DateUtil.java
│       ├── CurrencyUtil.java
│       └── ValidationUtil.java
├── src/main/resources/
│   ├── application.yml
│   ├── application-dev.yml
│   ├── application-prod.yml
│   └── db/migration/
│       ├── V1__init_schema.sql
│       ├── V2__seed_data.sql
│       └── V3__add_indexes.sql
└── src/test/java/com/expensetracker/
    ├── controller/
    ├── service/
    └── repository/
```

---

## 7. Deployment Architecture

```mermaid
graph TB
    subgraph "User Devices"
        Browser[Web Browser]
        Mobile[Mobile Browser]
    end
    
    subgraph "CDN / Edge"
        Vercel[Vercel CDN<br/>Static Assets]
    end
    
    subgraph "Backend Infrastructure"
        LB[Load Balancer<br/>Nginx/Railway]
        
        subgraph "Application Tier"
            API1[Spring Boot<br/>Instance 1]
            API2[Spring Boot<br/>Instance 2]
        end
        
        subgraph "Data Tier"
            PrimaryDB[(PostgreSQL<br/>Primary)]
            ReplicaDB[(PostgreSQL<br/>Read Replica)]
            Redis[(Redis Cache)]
        end
        
        subgraph "External Services"
            S3[AWS S3<br/>File Storage]
            SMTP[Email Service<br/>SendGrid]
        end
    end
    
    Browser -->|HTTPS| Vercel
    Mobile -->|HTTPS| Vercel
    
    Vercel -->|API Calls<br/>HTTPS| LB
    
    LB --> API1
    LB --> API2
    
    API1 -->|Write| PrimaryDB
    API2 -->|Write| PrimaryDB
    
    API1 -->|Read| ReplicaDB
    API2 -->|Read| ReplicaDB
    
    API1 --> Redis
    API2 --> Redis
    
    API1 --> S3
    API2 --> S3
    
    API1 --> SMTP
    
    PrimaryDB -.Replication.-> ReplicaDB
    
    style Vercel fill:#000000,stroke:#000000,color:#ffffff
    style LB fill:#269b47,stroke:#1a7a35,color:#ffffff
    style API1 fill:#6db33f,stroke:#4e8b2f,color:#ffffff
    style API2 fill:#6db33f,stroke:#4e8b2f,color:#ffffff
    style PrimaryDB fill:#336791,stroke:#264e71,color:#ffffff
    style ReplicaDB fill:#336791,stroke:#264e71,color:#ffffff
```

---

## 8. Authentication Flow

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant API
    participant DB
    participant JWT

    User->>Frontend: Enter credentials
    Frontend->>API: POST /auth/login
    API->>DB: Validate credentials
    DB-->>API: User found
    API->>JWT: Generate token
    JWT-->>API: JWT token
    API-->>Frontend: 200 OK + token
    Frontend->>Frontend: Store token in localStorage
    
    Note over Frontend,API: Subsequent Requests
    
    User->>Frontend: Access protected page
    Frontend->>API: GET /transactions<br/>Header: Authorization: Bearer {token}
    API->>JWT: Validate token
    JWT-->>API: Token valid + user info
    API->>DB: Fetch transactions
    DB-->>API: Transaction data
    API-->>Frontend: 200 OK + data
    Frontend->>User: Display transactions
```

---

## 9. Transaction Creation Flow

```mermaid
sequenceDiagram
    participant User
    participant TransactionForm
    participant TanStackQuery
    participant API
    participant TransactionService
    participant RecurringService
    participant DB

    User->>TransactionForm: Fill form & submit
    TransactionForm->>TransactionForm: Validate with Zod
    TransactionForm->>TanStackQuery: mutate(transactionData)
    TanStackQuery->>API: POST /transactions
    API->>TransactionService: createTransaction()
    TransactionService->>DB: INSERT transaction
    DB-->>TransactionService: Transaction created
    TransactionService->>RecurringService: detectPattern()
    RecurringService-->>TransactionService: Pattern detected
    TransactionService-->>API: Transaction + Pattern
    API-->>TanStackQuery: 201 Created
    TanStackQuery->>TanStackQuery: Invalidate cache
    TanStackQuery-->>TransactionForm: Success
    TransactionForm->>User: Show success toast
```

---

## 10. Budget Alert Flow

```mermaid
flowchart TD
    A[Transaction Created] --> B{Check Budget}
    B --> C[Calculate Current Spending]
    C --> D{Spending >= Alert Threshold?}
    D -->|Yes| E[Create Alert Event]
    D -->|No| F[No Action]
    E --> G{Alert Enabled?}
    G -->|Yes| H[Send Email Notification]
    G -->|No| F
    H --> I[Update Alert Status]
    I --> J[End]
    F --> J
```

---

## 11. Recurring Pattern Detection Algorithm

```mermaid
flowchart TD
    Start[New Transaction Created] --> A[Fetch Last 6 Months<br/>Transactions]
    A --> B[Group by:<br/>Amount ± 10%<br/>Category<br/>Description similarity]
    B --> C{Found >= 3<br/>matching transactions?}
    C -->|No| End[No Pattern]
    C -->|Yes| D[Calculate Time Intervals]
    D --> E{Intervals consistent?<br/>e.g., ~30 days apart}
    E -->|No| End
    E -->|Yes| F[Calculate Confidence Score]
    F --> G[Create/Update<br/>Recurring Pattern]
    G --> H[Predict Next Date]
    H --> I[Save Pattern to DB]
    I --> End2[Pattern Detected]
    
    style Start fill:#4caf50,stroke:#2e7d32,color:#ffffff
    style End2 fill:#4caf50,stroke:#2e7d32,color:#ffffff
    style End fill:#f44336,stroke:#c62828,color:#ffffff
```

---

## 12. Database ER Diagram (Simplified)

```mermaid
erDiagram
    users ||--o{ user_households : "member of"
    households ||--o{ user_households : "has"
    households ||--o{ transactions : "contains"
    households ||--o{ budgets : "has"
    households ||--o{ categories : "defines"
    users ||--o{ transactions : "created by"
    categories ||--o{ transactions : "categorizes"
    budgets ||--o{ budget_categories : "tracks"
    categories ||--o{ budget_categories : "included in"
    
    users {
        bigint id PK
        string email UK
        string password_hash
        string full_name
        string role
    }
    
    households {
        bigint id PK
        string name
        string currency
    }
    
    transactions {
        bigint id PK
        bigint household_id FK
        bigint user_id FK
        bigint category_id FK
        decimal amount
        string type
        date transaction_date
    }
    
    budgets {
        bigint id PK
        bigint household_id FK
        decimal amount
        date start_date
        date end_date
    }
    
    categories {
        bigint id PK
        bigint household_id FK
        string name
        string type
    }
```

---

## 13. CI/CD Pipeline Flow

```mermaid
flowchart LR
    A[Git Push] --> B[GitHub Actions Triggered]
    
    subgraph "Frontend Pipeline"
        B --> C1[Install Dependencies]
        C1 --> D1[Run ESLint]
        D1 --> E1[Run Type Check]
        E1 --> F1[Run Unit Tests]
        F1 --> G1[Build Production]
        G1 --> H1[Deploy to Vercel]
    end
    
    subgraph "Backend Pipeline"
        B --> C2[Maven Build]
        C2 --> D2[Run Checkstyle]
        D2 --> E2[Run Unit Tests]
        E2 --> F2[Run Integration Tests]
        F2 --> G2[Build Docker Image]
        G2 --> H2[Push to Registry]
        H2 --> I2[Deploy to Railway]
    end
    
    style A fill:#4caf50,stroke:#2e7d32,color:#ffffff
    style H1 fill:#000000,stroke:#000000,color:#ffffff
    style I2 fill:#0b0d0e,stroke:#0b0d0e,color:#ffffff
```

---

## 14. Caching Strategy

```mermaid
flowchart TD
    Request[API Request] --> Cache{Check Redis Cache}
    Cache -->|Hit| Return[Return Cached Data]
    Cache -->|Miss| DB[Query Database]
    DB --> Store[Store in Cache<br/>TTL: 5 minutes]
    Store --> Return
    
    subgraph "Cache Invalidation"
        Mutation[Create/Update/Delete] --> Invalidate[Invalidate Related Keys]
        Invalidate --> Pattern1[transactions:household:*]
        Invalidate --> Pattern2[budgets:household:*]
        Invalidate --> Pattern3[analytics:household:*]
    end
    
    style Cache fill:#ff6b6b,stroke:#c92a2a,color:#ffffff
    style Mutation fill:#fab005,stroke:#e67700,color:#000000
```

---

## 15. Security Layers

```mermaid
flowchart TD
    Request[HTTP Request] --> HTTPS{HTTPS Only}
    HTTPS -->|Encrypted| CORS{CORS Check}
    CORS -->|Allowed Origin| RateLimit{Rate Limiting}
    RateLimit -->|Within Limit| JWT{JWT Validation}
    JWT -->|Valid Token| RBAC{Role Check}
    RBAC -->|Authorized| Input{Input Validation}
    Input -->|Valid| SQL{Parameterized Queries}
    SQL --> Business[Business Logic]
    
    HTTPS -->|Not HTTPS| Reject1[403 Forbidden]
    CORS -->|Invalid Origin| Reject1
    RateLimit -->|Exceeded| Reject2[429 Too Many Requests]
    JWT -->|Invalid/Expired| Reject3[401 Unauthorized]
    RBAC -->|Insufficient Perms| Reject4[403 Forbidden]
    Input -->|Invalid| Reject5[400 Bad Request]
    
    style Business fill:#4caf50,stroke:#2e7d32,color:#ffffff
    style Reject1 fill:#f44336,stroke:#c62828,color:#ffffff
    style Reject2 fill:#f44336,stroke:#c62828,color:#ffffff
    style Reject3 fill:#f44336,stroke:#c62828,color:#ffffff
    style Reject4 fill:#f44336,stroke:#c62828,color:#ffffff
    style Reject5 fill:#f44336,stroke:#c62828,color:#ffffff
```

---

## 16. Responsive Design Breakpoints

```
Mobile First Approach:

┌─────────────────────────────────────────────────┐
│ xs: 0px - 639px (Mobile)                        │
│ - Single column layout                          │
│ - Bottom navigation                             │
│ - Collapsible filters                           │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ sm: 640px - 767px (Large Mobile / Small Tablet) │
│ - Two column grid (cards)                       │
│ - Side navigation drawer                        │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ md: 768px - 1023px (Tablet)                     │
│ - Sidebar visible                               │
│ - Three column grid                             │
│ - Expanded charts                               │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ lg: 1024px - 1279px (Desktop)                   │
│ - Full sidebar                                  │
│ - Multi-column layouts                          │
│ - All features visible                          │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ xl: 1280px+ (Large Desktop)                     │
│ - Maximum width container (1280px)              │
│ - Optimized spacing                             │
└─────────────────────────────────────────────────┘
```

---

## 17. State Management Architecture

```mermaid
flowchart TB
    subgraph "Global State"
        AuthContext[Auth Context<br/>User, Token, Logout]
        HouseholdContext[Household Context<br/>Current Household]
    end
    
    subgraph "Server State - TanStack Query"
        Transactions[Transactions Query]
        Budgets[Budgets Query]
        Categories[Categories Query]
        Analytics[Analytics Query]
    end
    
    subgraph "Local State"
        Forms[Form State<br/>React Hook Form]
        UI[UI State<br/>Modal, Drawer, Toast]
    end
    
    Components[React Components] --> AuthContext
    Components --> HouseholdContext
    Components --> Transactions
    Components --> Budgets
    Components --> Categories
    Components --> Analytics
    Components --> Forms
    Components --> UI
    
    Transactions --> API[Backend API]
    Budgets --> API
    Categories --> API
    Analytics --> API
    
    style AuthContext fill:#61dafb,stroke:#21a1c4,color:#000000
    style Transactions fill:#ff4154,stroke:#c91f2e,color:#ffffff
```

---

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | React 18 + TypeScript | UI framework |
| | Vite | Build tool & dev server |
| | TailwindCSS | Utility-first styling |
| | shadcn/ui | Component library |
| | TanStack Query | Server state management |
| | React Router | Client-side routing |
| | Recharts | Data visualization |
| | React Hook Form + Zod | Form handling & validation |
| **Backend** | Spring Boot 3.2 | Application framework |
| | Spring Security 6 | Authentication & authorization |
| | Spring Data JPA | ORM & database access |
| | JJWT | JWT token generation |
| | Flyway | Database migrations |
| | Springdoc OpenAPI | API documentation |
| **Database** | PostgreSQL 15+ | Relational database |
| | Redis | Caching layer |
| **DevOps** | Docker | Containerization |
| | GitHub Actions | CI/CD pipeline |
| | Vercel | Frontend hosting |
| | Railway/Render | Backend hosting |
| | AWS S3 | File storage |

---

**Document Version:** 1.0  
**Last Updated:** August 4, 2026  
**Owner:** Architecture Team
