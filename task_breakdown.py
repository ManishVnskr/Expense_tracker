"""
Task Breakdown Content for PDF Generation
"""

def add_task_breakdown(pdf):
    """Add comprehensive task breakdown to the PDF"""
    
    pdf.add_page()
    pdf.chapter_title('Implementation Task Breakdown', 1)
    
    intro_text = """The implementation is divided into 30 sequential tasks, organized into logical phases. Each task includes clear objectives, implementation steps, testing strategies, and deliverable demos."""
    pdf.chapter_body(intro_text)
    
    # Task 1
    pdf.chapter_title('Task 1: Project Initialization and Setup', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Objective:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Set up foundational structure for frontend and backend with proper tooling')
    pdf.ln(2)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Implementation Steps:', 0, 1)
    task1_steps = [
        "Initialize Spring Boot 3.2+ with dependencies: Web, Security, JPA, PostgreSQL, Flyway, Lombok, Validation, Springdoc",
        "Initialize Vite + React + TypeScript with strict configuration",
        "Configure Tailwind CSS and install shadcn/ui CLI",
        "Set up ESLint, Prettier for frontend; Checkstyle for backend",
        "Create .env.example files with required environment variables",
        "Initialize Git repositories (separate for frontend and backend)",
        "Configure basic CI workflows for linting and build checks"
    ]
    pdf.add_bullet_list(task1_steps)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Testing:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Verify builds succeed, linting passes, development servers start without errors')
    pdf.ln(3)
    
    # Task 2
    pdf.chapter_title('Task 2: Database Schema Design and Migration Setup', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Objective:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Design complete database schema with Flyway migrations')
    pdf.ln(2)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Implementation Steps:', 0, 1)
    task2_steps = [
        "Create Flyway migration directory structure",
        "V1__create_users_table.sql: id, email, password_hash, first_name, last_name, timestamps",
        "V2__create_households_and_user_households.sql: households, user_households with role enum",
        "V3__create_categories_table.sql: with icons, colors, type enum",
        "V4__create_transactions_table.sql: with tags array, foreign keys",
        "V5__create_budgets_and_alerts.sql: budgets with rollover support",
        "V6__create_recurring_patterns_table.sql: pattern detection metadata",
        "Add indexes: user_id, household_id, transaction_date, category_id",
        "R__seed_default_categories.sql: repeatable migration for default data"
    ]
    pdf.add_bullet_list(task2_steps)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Testing:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Run migrations against local PostgreSQL, verify schema correctness, check foreign key constraints')
    pdf.ln(3)
    
    # Task 3
    pdf.add_page()
    pdf.chapter_title('Task 3: Docker Compose Local Development Environment', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Objective:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Create complete Docker Compose setup for local development')
    pdf.ln(2)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Implementation Steps:', 0, 1)
    task3_steps = [
        "Create docker-compose.yml with PostgreSQL service (persistent volume, health check)",
        "Configure environment variables for database credentials",
        "Add spring-boot-docker-compose dependency to backend",
        "Create application-dev.yml for Docker connection",
        "Create application-local.yml for local PostgreSQL",
        "Add pgAdmin service for database management",
        "Create startup scripts for migrations and seed data",
        "Document connection strings in README"
    ]
    pdf.add_bullet_list(task3_steps)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Testing:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Start Docker Compose, verify PostgreSQL accessible, Spring Boot connects, migrations run')
    pdf.ln(3)
    
    # Task 4-6
    add_backend_core_tasks(pdf)
    
    # Task 7-13
    add_backend_api_tasks(pdf)
    
    # Task 14-15
    add_backend_testing_tasks(pdf)
    
    # Task 16-24
    add_frontend_tasks(pdf)
    
    # Task 25-30
    add_deployment_tasks(pdf)


def add_backend_core_tasks(pdf):
    """Add backend core infrastructure tasks"""
    
    # Task 4
    pdf.chapter_title('Task 4: Backend - User Entity and Repository Layer', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Objective:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Create JPA entities and repository interfaces for core domain model')
    pdf.ln(2)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Key Entities:', 0, 1)
    entities = [
        "User: Authentication and profile data",
        "Household: Shared workspace for expense tracking",
        "UserHousehold: Join table with role enum (OWNER, ADMIN, VIEWER)",
        "Category: Expense/income categories with icons and colors",
        "Transaction: Financial records with tags and relationships",
        "RecurringPattern: Detected recurring transaction metadata",
        "Budget & BudgetAlert: Budget limits and notifications"
    ]
    pdf.add_bullet_list(entities)
    pdf.ln(2)
    
    # Task 5
    pdf.add_page()
    pdf.chapter_title('Task 5: Backend - JWT Authentication Service', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Objective:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Implement JWT-based authentication with registration and login')
    pdf.ln(2)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Components:', 0, 1)
    jwt_components = [
        "JwtService: Token generation and validation using JJWT library",
        "AuthenticationService: Registration and login business logic",
        "UserDetailsService: Load users from database for authentication",
        "JwtAuthenticationFilter: Validate tokens on each request",
        "SecurityFilterChain: Configure public and protected endpoints",
        "PasswordEncoder: BCrypt with strength 12",
        "DTOs: RegisterRequest, LoginRequest, AuthenticationResponse",
        "AuthenticationController: /api/auth/register and /api/auth/login endpoints"
    ]
    pdf.add_bullet_list(jwt_components)
    pdf.ln(2)
    
    # Task 6
    pdf.chapter_title('Task 6: Backend - Role-Based Access Control (RBAC)', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Objective:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 5, 'Implement granular permission checking for household-shared resources')
    pdf.ln(2)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Implementation:', 0, 1)
    rbac_impl = [
        "@PreAuthorize expressions for declarative security",
        "Custom PermissionEvaluator for household-specific checks",
        "HouseholdPermissionService: canView(), canEdit(), canDelete(), canManageMembers()",
        "Aspect for automatic household context injection from JWT",
        "@CurrentUser annotation for injecting authenticated user",
        "ResourceAccessDeniedException with global exception handler",
        "Method security configuration enabled"
    ]
    pdf.add_bullet_list(rbac_impl)
    pdf.ln(3)


def add_backend_api_tasks(pdf):
    """Add backend API development tasks"""
    
    # Task 7
    pdf.add_page()
    pdf.chapter_title('Task 7: Backend - Household Management API', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Endpoints:', 0, 1)
    household_endpoints = [
        "POST /api/households - Create household (user becomes OWNER)",
        "GET /api/households - List user's households",
        "GET /api/households/{id} - Get household details",
        "POST /api/households/{id}/members - Invite member (OWNER/ADMIN)",
        "PATCH /api/households/{id}/members/{userId} - Update role (OWNER only)",
        "DELETE /api/households/{id}/members/{userId} - Remove member (OWNER/ADMIN)"
    ]
    pdf.add_bullet_list(household_endpoints)
    pdf.ln(2)
    
    # Task 8
    pdf.chapter_title('Task 8: Backend - Category Management API', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Features:', 0, 1)
    category_features = [
        "CRUD operations for personal and household categories",
        "Icon picker integration with predefined icon set",
        "Color palette with customizable color selection",
        "Default system categories with special handling",
        "Category usage tracking (transaction count)",
        "Validation preventing deletion of categories with transactions"
    ]
    pdf.add_bullet_list(category_features)
    pdf.ln(2)
    
    # Task 9
    pdf.chapter_title('Task 9: Backend - Transaction Management API', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Advanced Features:', 0, 1)
    transaction_features = [
        "Dynamic filtering using JPA Criteria API or QueryDSL",
        "Filters: date range, category, type, tags, amount range, description search",
        "Pagination and sorting support (by date, amount, category)",
        "Tag management with PostgreSQL array field",
        "Bulk operations for efficient data management",
        "Transaction validation rules (amount > 0, valid date, etc.)"
    ]
    pdf.add_bullet_list(transaction_features)
    pdf.ln(2)
    
    # Task 10
    pdf.add_page()
    pdf.chapter_title('Task 10: Backend - Recurring Transaction Detection', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Algorithm Steps:', 0, 1)
    recurring_algo = [
        "Group transactions by similar merchant names (fuzzy matching)",
        "Identify recurring intervals: weekly (7±3 days), monthly (30±5 days), quarterly (90±7 days)",
        "Calculate average amounts with ±10% tolerance",
        "Compute confidence scores based on pattern consistency (0-1 scale)",
        "Store detected patterns with next expected date",
        "Scheduled job runs daily to detect new patterns",
        "Auto-create transactions for confirmed patterns",
        "User can confirm, dismiss, or disable auto-creation"
    ]
    pdf.add_bullet_list(recurring_algo)
    pdf.ln(2)
    
    # Task 11
    pdf.chapter_title('Task 11: Backend - Budget Management with Rollover', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Key Features:', 0, 1)
    budget_features = [
        "Monthly category-based budget limits",
        "Rollover calculation: unused amount carries to next month",
        "Alert thresholds: WARNING (80%), EXCEEDED (100%)",
        "Budget templates: save and apply configurations",
        "Scheduled job for month-end rollover processing",
        "Budget vs. actual spending comparison",
        "Historical budget tracking and trends"
    ]
    pdf.add_bullet_list(budget_features)
    pdf.ln(2)
    
    # Task 12
    pdf.chapter_title('Task 12: Backend - Analytics and Insights Service', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Analytics Endpoints:', 0, 1)
    analytics_endpoints = [
        "GET /api/analytics/dashboard - Summary metrics",
        "GET /api/analytics/category-breakdown - Category spending percentages",
        "GET /api/analytics/monthly-trends - 12-month income vs. expense",
        "GET /api/analytics/predictions - Rule-based spending forecasts"
    ]
    pdf.add_bullet_list(analytics_endpoints)
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Prediction Algorithms:', 0, 1)
    predictions = [
        "Simple moving average: 3-month average for category forecast",
        "Trend detection: identify increasing/decreasing/stable patterns",
        "Anomaly detection: flag transactions >2 standard deviations from mean",
        "Seasonal patterns: identify recurring seasonal spending changes"
    ]
    pdf.add_bullet_list(predictions)
    pdf.ln(2)
    
    # Task 13
    pdf.add_page()
    pdf.chapter_title('Task 13: Backend - Export Service (CSV and PDF)', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Export Functionality:', 0, 1)
    export_features = [
        "CSV export: Transactions with all filters applied",
        "PDF report: Transaction list with summary statistics",
        "PDF budget report: Monthly budget vs. actual with charts",
        "Streaming response for large datasets",
        "Custom date range selection",
        "Formatted currency and date display",
        "Chart images embedded in PDF using chart libraries"
    ]
    pdf.add_bullet_list(export_features)
    pdf.ln(3)


def add_backend_testing_tasks(pdf):
    """Add backend testing tasks"""
    
    # Task 14
    pdf.chapter_title('Task 14: Backend - API Documentation with Swagger', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Documentation Features:', 0, 1)
    swagger_features = [
        "Springdoc OpenAPI 2.x integration",
        "Bearer token authentication in Swagger UI",
        "@Operation and @ApiResponse annotations on endpoints",
        "@Schema annotations on DTOs with examples",
        "API grouping by tags: Auth, Households, Transactions, etc.",
        "Interactive testing directly from Swagger UI",
        "OpenAPI 3.0 specification generation"
    ]
    pdf.add_bullet_list(swagger_features)
    pdf.ln(2)
    
    # Task 15
    pdf.chapter_title('Task 15: Backend - Integration Tests and Coverage', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Testing Strategy:', 0, 1)
    testing_strategy = [
        "Testcontainers for PostgreSQL in test environment",
        "@SpringBootTest with MockMvc for controller tests",
        "Test authentication flows: register, login, token validation",
        "Test RBAC scenarios: different roles accessing resources",
        "Test transaction filtering with complex queries",
        "Test recurring pattern detection with sample data",
        "Test budget rollover and alert triggering",
        "REST Assured for API integration testing",
        "JaCoCo for code coverage reports (target: >80%)"
    ]
    pdf.add_bullet_list(testing_strategy)
    pdf.ln(3)


def add_frontend_tasks(pdf):
    """Add frontend development tasks"""
    
    pdf.add_page()
    pdf.chapter_title('Task 16: Frontend - Project Setup and UI Foundation', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Setup Steps:', 0, 1)
    frontend_setup = [
        "Initialize Vite + React + TypeScript project",
        "Configure Tailwind CSS with custom design tokens",
        "Install shadcn/ui base components: Button, Card, Input, Dialog, etc.",
        "Set up React Router with protected and public routes",
        "Create ProtectedRoute wrapper for authentication",
        "Build layout components: AppLayout, Sidebar, Header",
        "Configure path aliases in tsconfig and vite.config"
    ]
    pdf.add_bullet_list(frontend_setup)
    pdf.ln(2)
    
    # Task 17
    pdf.chapter_title('Task 17: Frontend - API Client and TanStack Query', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Configuration:', 0, 1)
    api_config = [
        "Create Axios instance with base URL from environment",
        "Request interceptor: attach JWT token from localStorage",
        "Response interceptor: handle 401 errors (redirect to login)",
        "QueryClient with default options (staleTime, retry)",
        "Hierarchical query keys for cache organization",
        "API service layer with typed methods",
        "Centralized error handling with Error Boundary",
        "AuthContext for user state and token management"
    ]
    pdf.add_bullet_list(api_config)
    pdf.ln(2)
    
    # Task 18
    pdf.chapter_title('Task 18: Frontend - Authentication UI', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Components:', 0, 1)
    auth_components = [
        "LoginPage: Email/password form with validation",
        "RegisterPage: Name, email, password, confirm password",
        "Zod schemas for client-side validation",
        "React Hook Form integration for form state",
        "useLogin and useRegister mutation hooks",
        "Error handling with user-friendly messages",
        "Loading states with disabled form controls",
        "Password visibility toggle",
        "Redirect to dashboard after successful authentication"
    ]
    pdf.add_bullet_list(auth_components)
    pdf.ln(2)
    
    # Task 19-24
    pdf.add_page()
    pdf.chapter_title('Task 19: Frontend - Dashboard Page', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Dashboard Features:', 0, 1)
    dashboard_features = [
        "Summary cards: Total Balance, Monthly Income, Monthly Expense, Top Category",
        "useDashboardSummary query hook with caching",
        "Loading skeletons with shadcn/ui Skeleton",
        "Error state with retry button",
        "Household selector dropdown for multi-household users",
        "Date range picker (default: current month)",
        "Percentage change indicators with trend arrows",
        "Responsive grid layout"
    ]
    pdf.add_bullet_list(dashboard_features)
    pdf.ln(2)
    
    pdf.chapter_title('Task 20: Frontend - Transaction List with Filters', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Features:', 0, 1)
    transaction_list = [
        "useTransactions query hook with filter parameters",
        "Filter panel: date range, category, type, amount range, search",
        "shadcn/ui Table component for transaction display",
        "Pagination controls with page size selector",
        "Column sorting (click headers to sort)",
        "Row actions: Edit, Delete with confirmation dialog",
        "TransactionDialog for create/edit with validation",
        "Optimistic updates using TanStack Query mutations",
        "Empty state when no transactions found"
    ]
    pdf.add_bullet_list(transaction_list)
    pdf.ln(2)
    
    pdf.chapter_title('Task 21: Frontend - Category Management', 2)
    pdf.chapter_title('Task 22: Frontend - Budget Management', 2)
    pdf.chapter_title('Task 23: Frontend - Analytics and Charts', 2)
    pdf.chapter_title('Task 24: Frontend - Household Management', 2)
    
    summary = """Tasks 21-24 follow similar patterns: query hooks for data fetching, shadcn/ui components for UI, React Hook Form for forms, and TanStack Query for state management. Each includes comprehensive error handling, loading states, and optimistic updates."""
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 5, summary)
    pdf.ln(3)


def add_deployment_tasks(pdf):
    """Add deployment and finalization tasks"""
    
    pdf.add_page()
    pdf.chapter_title('Task 25: Frontend - Testing and Coverage', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Testing Approach:', 0, 1)
    frontend_testing = [
        "Vitest for unit tests with React Testing Library",
        "MSW (Mock Service Worker) for API mocking",
        "Component tests for all major UI components",
        "Form validation tests with various inputs",
        "Integration tests for user flows (login -> dashboard -> create transaction)",
        "Accessibility tests with jest-axe",
        "Coverage reports with Istanbul (target: >75%)"
    ]
    pdf.add_bullet_list(frontend_testing)
    pdf.ln(2)
    
    pdf.chapter_title('Task 26: Dockerization and Local Deployment', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Docker Setup:', 0, 1)
    docker_setup = [
        "Create Dockerfile for Spring Boot (multi-stage build)",
        "Create Dockerfile for React (Nginx serving static files)",
        "Update docker-compose.yml with all services",
        "Environment variable configuration for each service",
        "Health checks for all containers",
        "Persistent volumes for PostgreSQL data",
        "Docker network for service communication"
    ]
    pdf.add_bullet_list(docker_setup)
    pdf.ln(2)
    
    pdf.chapter_title('Task 27: CI/CD Pipeline Setup', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'GitHub Actions Workflows:', 0, 1)
    cicd_workflows = [
        "Backend: Lint, test, build, Docker image push",
        "Frontend: Lint, test, build, deploy to Vercel/Netlify",
        "Automated testing on pull requests",
        "Code coverage reporting with Codecov",
        "Automated dependency updates with Dependabot",
        "Security scanning with Snyk or GitHub Security"
    ]
    pdf.add_bullet_list(cicd_workflows)
    pdf.ln(2)
    
    pdf.chapter_title('Task 28: Backend Deployment to Railway/Render', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Deployment Steps:', 0, 1)
    backend_deploy = [
        "Create Railway/Render account and project",
        "Configure environment variables (database URL, JWT secret)",
        "Set up managed PostgreSQL database",
        "Deploy backend from Docker image or Git repository",
        "Configure custom domain (optional)",
        "Set up health check endpoints",
        "Configure automatic deployments from main branch",
        "Test API endpoints with Swagger UI"
    ]
    pdf.add_bullet_list(backend_deploy)
    pdf.ln(2)
    
    pdf.chapter_title('Task 29: Frontend Deployment to Vercel/Netlify', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Deployment Steps:', 0, 1)
    frontend_deploy = [
        "Connect Git repository to Vercel/Netlify",
        "Configure build command and output directory",
        "Set environment variables (API base URL)",
        "Configure rewrites for client-side routing",
        "Set up custom domain (optional)",
        "Enable automatic deployments from main branch",
        "Configure preview deployments for PRs",
        "Test deployed application end-to-end"
    ]
    pdf.add_bullet_list(frontend_deploy)
    pdf.ln(2)
    
    pdf.add_page()
    pdf.chapter_title('Task 30: Documentation and Project Finalization', 2)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, 'Documentation:', 0, 1)
    documentation = [
        "README.md with project overview, setup instructions",
        "Architecture documentation with diagrams",
        "API documentation (Swagger + additional notes)",
        "Database schema documentation",
        "Deployment guide for each environment",
        "Contributing guidelines",
        "Security considerations and best practices",
        "Performance optimization notes",
        "Troubleshooting guide",
        "Demo video or screenshots"
    ]
    pdf.add_bullet_list(documentation)
    pdf.ln(3)
    
    # Summary
    pdf.chapter_title('Implementation Timeline', 2)
    timeline_text = """Estimated timeline for full implementation:

Phase 1 - Foundation (Tasks 1-6): 2-3 weeks
- Project setup, database design, authentication, RBAC

Phase 2 - Backend APIs (Tasks 7-13): 3-4 weeks
- Core APIs, recurring detection, budgets, analytics, exports

Phase 3 - Backend Testing (Tasks 14-15): 1 week
- Documentation, comprehensive testing, coverage

Phase 4 - Frontend Core (Tasks 16-20): 2-3 weeks
- Setup, authentication UI, dashboard, transactions

Phase 5 - Frontend Features (Tasks 21-24): 2-3 weeks
- Categories, budgets, analytics, households

Phase 6 - Testing & Deployment (Tasks 25-30): 2 weeks
- Frontend testing, Docker, CI/CD, deployment, documentation

Total Estimated Time: 12-16 weeks (3-4 months) for complete implementation

This timeline assumes a single full-time developer. With a team or part-time work, adjust accordingly."""
    
    pdf.chapter_body(timeline_text)
