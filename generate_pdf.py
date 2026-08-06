#!/usr/bin/env python3
"""
PDF Generator for Expense Tracker Implementation Plan
"""

from fpdf import FPDF
import textwrap
from datetime import datetime


class ExpenseTrackerPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Expense Tracker - Implementation Plan', 0, 1, 'C')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        
    def chapter_title(self, title, level=1):
        if level == 1:
            self.set_font('Arial', 'B', 16)
            self.set_fill_color(52, 152, 219)
            self.set_text_color(255, 255, 255)
            self.cell(0, 10, title, 0, 1, 'L', True)
            self.set_text_color(0, 0, 0)
            self.ln(4)
        elif level == 2:
            self.set_font('Arial', 'B', 14)
            self.set_fill_color(230, 230, 230)
            self.cell(0, 8, title, 0, 1, 'L', True)
            self.ln(3)
        elif level == 3:
            self.set_font('Arial', 'B', 12)
            self.cell(0, 7, title, 0, 1, 'L')
            self.ln(2)
            
    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        # Use multi_cell directly without manual wrapping
        self.multi_cell(0, 5, body)
        self.ln(2)
        
    def add_bullet_list(self, items):
        self.set_font('Arial', '', 10)
        left_margin = self.l_margin
        for item in items:
            # Set position for bullet
            self.set_x(left_margin)
            # Add bullet
            self.cell(7, 5, chr(149), 0, 0)
            # Set position for text after bullet
            self.set_x(left_margin + 7)
            # Calculate available width
            available_width = self.w - left_margin - 7 - self.r_margin
            # Add text with multi_cell using the available width
            self.multi_cell(available_width, 5, item)
        self.ln(2)
        
    def add_numbered_list(self, items):
        self.set_font('Arial', '', 10)
        left_margin = self.l_margin
        for i, item in enumerate(items, 1):
            # Set position for number
            self.set_x(left_margin)
            # Add number
            self.cell(10, 5, f'{i}.', 0, 0)
            # Set position for text after number
            self.set_x(left_margin + 10)
            # Calculate available width
            available_width = self.w - left_margin - 10 - self.r_margin
            # Add text with multi_cell
            self.multi_cell(available_width, 5, item)
        self.ln(2)


def generate_pdf():
    pdf = ExpenseTrackerPDF()
    pdf.add_page()
    
    # Title Page
    pdf.set_font('Arial', 'B', 24)
    pdf.ln(40)
    pdf.cell(0, 15, 'Expense Tracker Application', 0, 1, 'C')
    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, 10, 'Full-Stack Implementation Plan', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 8, f'Generated: {datetime.now().strftime("%B %d, %Y")}', 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font('Arial', 'I', 11)
    pdf.multi_cell(0, 6, 'A production-ready, cloud-deployable expense tracker with multi-user collaboration, role-based access control, recurring transaction detection, advanced budget management, and comprehensive analytics.', 0, 'C')
    
    # Add content sections
    add_problem_statement(pdf)
    add_requirements(pdf)
    add_background(pdf)
    add_solution_architecture(pdf)
    add_tech_stack(pdf)
    
    return pdf


def add_problem_statement(pdf):
    pdf.add_page()
    pdf.chapter_title('Problem Statement', 1)
    
    problem_text = """Build a production-ready, cloud-deployable expense tracker application that supports multi-user collaboration with role-based access control. The system must handle complex financial workflows including recurring transaction detection, advanced budget management with rollover capabilities, predictive spending insights, and comprehensive data visualization with export functionality.

The application should enable users to:
- Track personal and shared household expenses
- Collaborate with family members or groups with granular permissions
- Automatically detect and manage recurring transactions
- Set and monitor budgets with rollover capabilities
- Gain insights through analytics and predictions
- Export financial data in multiple formats"""
    
    pdf.chapter_body(problem_text)


def add_requirements(pdf):
    pdf.chapter_title('Requirements', 1)
    
    pdf.chapter_title('Functional Requirements', 2)
    
    pdf.chapter_title('1. Authentication & Authorization', 3)
    auth_requirements = [
        "JWT-based stateless authentication with access tokens",
        "Role-based access control (Owner/Admin/Viewer) for shared resources",
        "User registration and login with secure password hashing (BCrypt)",
        "Token validation and refresh mechanisms"
    ]
    pdf.add_bullet_list(auth_requirements)
    
    pdf.chapter_title('2. Multi-User Sharing', 3)
    sharing_requirements = [
        "Users can create and manage household/group budgets",
        "Invite members with specific roles (Owner, Admin, Viewer)",
        "Granular permissions for viewing, editing, and deleting transactions",
        "Household member management and role updates"
    ]
    pdf.add_bullet_list(sharing_requirements)
    
    pdf.chapter_title('3. Transaction Management', 3)
    transaction_requirements = [
        "Full CRUD operations on expenses and income",
        "Category management with customizable icons and colors",
        "Advanced filtering (date ranges, categories, amount, transaction type)",
        "Recurring transaction detection and automation",
        "Tag system for flexible organization",
        "Search functionality by description and merchant name"
    ]
    pdf.add_bullet_list(transaction_requirements)
    
    pdf.chapter_title('4. Budget Features', 3)
    budget_requirements = [
        "Monthly category-based budget limits",
        "Budget rollover functionality for unused amounts",
        "Budget templates for reuse across months",
        "Overspending alerts and notifications (80% warning, 100% exceeded)",
        "Shared budgets across household members",
        "Historical budget tracking and analysis"
    ]
    pdf.add_bullet_list(budget_requirements)
    
    pdf.add_page()
    pdf.chapter_title('5. Analytics & Insights', 3)
    analytics_requirements = [
        "Dashboard with summary cards (balance, monthly income/expense, top categories)",
        "Category breakdown visualizations with pie charts",
        "Monthly trend analysis with line and bar charts",
        "Custom date range comparisons",
        "Rule-based predictive spending insights using pattern detection",
        "Recurring expense identification and forecasting",
        "Anomaly detection for unusual spending patterns"
    ]
    pdf.add_bullet_list(analytics_requirements)
    
    pdf.chapter_title('6. Export & Reporting', 3)
    export_requirements = [
        "CSV export for transactions with customizable filters",
        "PDF report generation with charts and summaries",
        "Customizable date range exports",
        "Budget reports showing spent vs. allocated amounts"
    ]
    pdf.add_bullet_list(export_requirements)
    
    pdf.chapter_title('Technical Requirements', 2)
    
    tech_requirements = [
        "Backend: Spring Boot 3.x, Java 17+, PostgreSQL 15+",
        "Frontend: React 18+, TypeScript 5.x, Vite, Tailwind CSS, shadcn/ui",
        "Testing: JUnit 5 + Mockito + Testcontainers (backend), Vitest + Testing Library (frontend)",
        "Database Migrations: Flyway for versioned schema management",
        "Deployment: Dockerized services with separate deployments",
        "Frontend Hosting: Vercel or Netlify",
        "Backend Hosting: Railway or Render",
        "Database: Managed PostgreSQL (Neon, Supabase, or Railway)",
        "Development: Docker Compose for local orchestration"
    ]
    pdf.add_bullet_list(tech_requirements)


def add_background(pdf):
    pdf.add_page()
    pdf.chapter_title('Background & Research Findings', 1)
    
    pdf.chapter_title('TanStack Query Best Practices', 2)
    tanstack_findings = [
        "Use hierarchical query keys for cache organization: ['transactions', userId, { filters }]",
        "Implement centralized error handling with QueryClient defaults",
        "Minimize useEffect/useState for server state management",
        "Implement optimistic updates for better user experience",
        "Proper TypeScript integration with typed query and mutation hooks",
        "Use staleTime and cacheTime strategically for performance"
    ]
    pdf.add_bullet_list(tanstack_findings)
    
    pdf.chapter_title('Spring Boot JWT Security', 2)
    jwt_findings = [
        "Custom JWT filter extending OncePerRequestFilter",
        "Stateless session management with Spring Security",
        "JJWT library (0.12.x) for token generation and validation",
        "BCrypt password encoding with appropriate strength (12)",
        "SecurityFilterChain with role-based endpoint protection",
        "Proper exception handling for authentication failures"
    ]
    pdf.add_bullet_list(jwt_findings)
    
    pdf.chapter_title('Flyway Migration Strategy', 2)
    flyway_findings = [
        "Versioned migrations with naming convention: V1__description.sql",
        "Separate migration user with elevated database privileges",
        "Application user with restricted CRUD permissions only",
        "Repeatable migrations (R__) for views and procedures",
        "Baseline existing databases before applying migrations",
        "Use checksums to detect manual schema changes"
    ]
    pdf.add_bullet_list(flyway_findings)
    
    pdf.chapter_title('Docker Compose Development', 2)
    docker_findings = [
        "Spring Boot's spring-boot-docker-compose dependency for auto-connection",
        "PostgreSQL with persistent volumes for data retention",
        "Health checks using pg_isready for proper startup sequencing",
        "depends_on with condition: service_healthy for reliability",
        "Environment-specific profiles (dev, test, prod)",
        "Separate networks for service isolation"
    ]
    pdf.add_bullet_list(docker_findings)
    
    pdf.add_page()
    pdf.chapter_title('Recurring Transaction Detection', 2)
    recurring_findings = [
        "Rule-based pattern matching for merchant names and amounts",
        "Configurable tolerance thresholds (±10% amount variance, ±3 days interval)",
        "Rolling window analysis examining 3-6 month transaction history",
        "Confidence scoring based on pattern consistency",
        "Support for weekly, monthly, quarterly, and annual patterns",
        "Fuzzy string matching (Levenshtein distance) for merchant name matching"
    ]
    pdf.add_bullet_list(recurring_findings)
    
    pdf.chapter_title('shadcn/ui Integration', 2)
    shadcn_findings = [
        "Copy-paste components directly into project (no external dependencies)",
        "Class Variance Authority (CVA) for flexible variant management",
        "Built on Radix UI primitives for accessibility compliance",
        "Tailwind CSS design tokens (primary, secondary, border, etc.)",
        "Compound component patterns for complex UI structures",
        "Easy customization through direct source code access"
    ]
    pdf.add_bullet_list(shadcn_findings)
    
    pdf.chapter_title('Role-Based Access Control', 2)
    rbac_findings = [
        "Spring Security @PreAuthorize expressions for method-level security",
        "Custom PermissionEvaluator for household-specific access checks",
        "Three-tier role system: Owner (full control), Admin (manage content), Viewer (read-only)",
        "Aspect-oriented approach for automatic household context injection",
        "Global exception handling for access denied scenarios",
        "Database-driven permissions for flexibility"
    ]
    pdf.add_bullet_list(rbac_findings)


def add_solution_architecture(pdf):
    pdf.add_page()
    pdf.chapter_title('Proposed Solution Architecture', 1)
    
    pdf.chapter_title('System Overview', 2)
    architecture_text = """The application follows a modern three-tier architecture with clear separation of concerns:

Frontend Layer: React-based SPA hosted on Vercel/Netlify, communicating with the backend via RESTful APIs. Uses TanStack Query for efficient data fetching and caching.

Backend Layer: Spring Boot REST API hosted on Railway/Render, handling business logic, authentication, and data persistence. Implements JWT-based stateless authentication.

Data Layer: Managed PostgreSQL database with Flyway-managed schema migrations, ensuring data consistency and versioning."""
    
    pdf.chapter_body(architecture_text)
    
    pdf.chapter_title('Key Architectural Decisions', 2)
    
    decisions = [
        "Stateless Authentication: JWT tokens eliminate server-side session storage, enabling horizontal scaling",
        "Separate Repositories: Frontend and backend maintained independently for clear ownership and deployment flexibility",
        "Role-Based Multi-Tenancy: Household model enables resource sharing while maintaining security boundaries",
        "Rule-Based Analytics: Simple algorithms for predictions avoid ML complexity while providing valuable insights",
        "Event-Driven Budget Alerts: Scheduled jobs check budget thresholds and trigger notifications asynchronously",
        "Optimistic UI Updates: Frontend updates immediately while backend processes requests in background"
    ]
    pdf.add_numbered_list(decisions)
    
    pdf.add_page()
    pdf.chapter_title('Database Schema Design', 2)
    
    schema_text = """The database schema is designed to support multi-user collaboration with clear ownership and permission boundaries:

Core Entities:
- Users: Authentication credentials and profile information
- Households: Shared workspaces for family/group expense tracking
- UserHouseholds: Join table with role assignments (Owner/Admin/Viewer)
- Categories: Expense/income categories with customization options
- Transactions: Financial records linked to users, households, and categories
- RecurringPatterns: Detected recurring transaction patterns
- Budgets: Monthly spending limits per category
- BudgetAlerts: Triggered notifications for budget thresholds

Key Relationships:
- One-to-Many: User -> Transactions, Household -> Budgets
- Many-to-Many: User <-> Household (through UserHouseholds with roles)
- One-to-Many: Category -> Transactions, Category -> Budgets
- One-to-Many: RecurringPattern -> Transactions"""
    
    pdf.chapter_body(schema_text)
    
    pdf.chapter_title('Security Architecture', 2)
    
    security_text = """Authentication Flow:
1. User submits credentials to /api/auth/login
2. Backend validates credentials against BCrypt hash
3. JWT token generated with user ID and roles as claims
4. Frontend stores token in localStorage
5. All subsequent requests include token in Authorization header
6. Backend validates token and extracts user context

Authorization Flow:
1. User attempts to access household resource
2. Backend extracts user ID from JWT token
3. Permission service checks user's role in target household
4. Access granted/denied based on role and operation type
5. Owner: Full access, Admin: Manage content, Viewer: Read-only"""
    
    pdf.chapter_body(security_text)


def add_tech_stack(pdf):
    pdf.add_page()
    pdf.chapter_title('Technology Stack', 1)
    
    pdf.chapter_title('Frontend Technologies', 2)
    
    frontend_stack = [
        "Build Tool: Vite 5.x - Fast development server with HMR",
        "Framework: React 18+ - Component-based UI library",
        "Language: TypeScript 5.x - Static typing for JavaScript",
        "Styling: Tailwind CSS 3.x - Utility-first CSS framework",
        "UI Components: shadcn/ui - Accessible components built on Radix UI",
        "State Management: TanStack Query v5 - Server state management",
        "HTTP Client: Axios - Promise-based HTTP client with interceptors",
        "Routing: React Router v6 - Declarative routing for React",
        "Forms: React Hook Form + Zod - Type-safe form validation",
        "Charts: Recharts - Composable charting library",
        "Icons: Lucide React - Consistent icon set",
        "Utilities: clsx, tailwind-merge - CSS class manipulation",
        "Notifications: Sonner - Toast notifications",
        "Testing: Vitest, Testing Library, MSW - Unit and integration testing"
    ]
    pdf.add_bullet_list(frontend_stack)
    
    pdf.chapter_title('Backend Technologies', 2)
    
    backend_stack = [
        "Framework: Spring Boot 3.2+ - Production-ready framework",
        "Language: Java 17+ - LTS version with modern features",
        "Security: Spring Security 6.x + JJWT 0.12.x - Authentication and authorization",
        "Data Access: Spring Data JPA + Hibernate 6.x - ORM and data persistence",
        "Database: PostgreSQL 15+ - Relational database with JSON support",
        "Migrations: Flyway 10.x - Database version control",
        "Validation: Jakarta Validation - Bean validation annotations",
        "Documentation: Springdoc OpenAPI 2.x - Swagger UI generation",
        "Utilities: Lombok - Boilerplate code reduction",
        "Mapping: MapStruct - Type-safe bean mapping",
        "Testing: JUnit 5, Mockito, Testcontainers, REST Assured"
    ]
    pdf.add_bullet_list(backend_stack)
    
    pdf.chapter_title('DevOps & Deployment', 2)
    
    devops_stack = [
        "Containerization: Docker - Application containerization",
        "Local Development: Docker Compose - Multi-container orchestration",
        "CI/CD: GitHub Actions - Automated testing and deployment",
        "Frontend Hosting: Vercel or Netlify - Static site hosting with CDN",
        "Backend Hosting: Railway or Render - Container-based hosting",
        "Database: Neon, Supabase, or Railway - Managed PostgreSQL",
        "Version Control: Git - Source code management"
    ]
    pdf.add_bullet_list(devops_stack)
    
    return pdf


if __name__ == '__main__':
    print("Generating PDF...")
    pdf = generate_pdf()
    output_path = '/home/govind/Desktop/project/Expense_Tracker.pdf'
    pdf.output(output_path)
    print(f"PDF generated successfully: {output_path}")
