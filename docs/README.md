# Expense Tracker - Supplementary Documentation

## 📋 Overview

This directory contains comprehensive technical documentation to supplement the **Expense_Tracker.pdf** implementation plan. These documents address the gaps identified by frontend, backend, DevOps, and QA perspectives.

**PDF Location:** `/home/govind/Desktop/project/Expense_Tracker.pdf`

---

## 📚 Documentation Index

| Document | Description | Audience |
|----------|-------------|----------|
| **[01_DATABASE_SCHEMA.md](./01_DATABASE_SCHEMA.md)** | Complete database design with ER diagrams, SQL DDL, indexes, views, triggers, and migration strategy | Backend, DBA |
| **[02_API_SPECIFICATION.md](./02_API_SPECIFICATION.md)** | REST API documentation with 36 endpoints, authentication flow, request/response examples, error handling | Backend, Frontend |
| **[03_ARCHITECTURE_DIAGRAMS.md](./03_ARCHITECTURE_DIAGRAMS.md)** | System architecture with C4 model diagrams, deployment architecture, component diagrams, folder structure | All teams |
| **[04_TEST_STRATEGY.md](./04_TEST_STRATEGY.md)** | Comprehensive testing strategy covering unit, integration, E2E, performance, and security testing | QA, All developers |
| **[05_DEVOPS_PIPELINE.md](./05_DEVOPS_PIPELINE.md)** | CI/CD pipeline, Docker configuration, deployment strategy, monitoring, disaster recovery | DevOps, Backend |

---

## 🎯 Quick Start Guide

### Prerequisites

Ensure you have the following installed:
- **Java 17+** (OpenJDK or Oracle JDK)
- **Node.js 18+** and npm
- **Maven 3.9+**
- **Docker 24+** and Docker Compose
- **PostgreSQL 15+** (or use Docker)
- **Git**

### Local Development Setup

**1. Clone Repository**
```bash
git clone https://github.com/your-org/expense-tracker.git
cd expense-tracker
```

**2. Start Infrastructure (Docker)**
```bash
docker-compose up -d postgres redis
```

**3. Backend Setup**
```bash
cd backend

# Install dependencies
mvn clean install

# Run database migrations
mvn flyway:migrate

# Start backend server
mvn spring-boot:run

# Backend will run on: http://localhost:8080
# API docs: http://localhost:8080/swagger-ui.html
```

**4. Frontend Setup**
```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev

# Frontend will run on: http://localhost:5173
```

**5. Verify Setup**
```bash
# Check backend health
curl http://localhost:8080/actuator/health

# Open frontend
open http://localhost:5173
```

---

## 🏗️ Project Structure

```
expense-tracker/
├── backend/                           # Spring Boot backend
│   ├── src/main/java/
│   │   └── com/expensetracker/
│   │       ├── controller/           # REST controllers
│   │       ├── service/              # Business logic
│   │       ├── repository/           # Data access layer
│   │       ├── model/                # Entities and DTOs
│   │       ├── security/             # JWT and auth
│   │       └── config/               # Spring configuration
│   ├── src/main/resources/
│   │   ├── db/migration/             # Flyway migrations
│   │   ├── application.yml           # Configuration
│   │   └── application-{env}.yml     # Environment configs
│   ├── src/test/                     # Tests
│   ├── pom.xml                       # Maven dependencies
│   └── Dockerfile                    # Container image
│
├── frontend/                          # React frontend
│   ├── src/
│   │   ├── components/               # React components
│   │   │   ├── ui/                   # shadcn/ui components
│   │   │   ├── transactions/
│   │   │   ├── budgets/
│   │   │   └── analytics/
│   │   ├── pages/                    # Page components
│   │   ├── api/                      # API client
│   │   ├── hooks/                    # Custom hooks
│   │   ├── contexts/                 # React contexts
│   │   ├── types/                    # TypeScript types
│   │   └── utils/                    # Utilities
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── docs/                              # Documentation
│   ├── 01_DATABASE_SCHEMA.md
│   ├── 02_API_SPECIFICATION.md
│   ├── 03_ARCHITECTURE_DIAGRAMS.md
│   ├── 04_TEST_STRATEGY.md
│   └── 05_DEVOPS_PIPELINE.md
│
├── .github/workflows/                 # CI/CD pipelines
│   ├── backend-ci-cd.yml
│   ├── frontend-ci-cd.yml
│   └── database-migration.yml
│
├── docker-compose.yml                 # Local development setup
├── README.md                          # This file
└── Expense_Tracker.pdf                # Original implementation plan
```

---

## 🔑 Key Technical Decisions

### Backend Architecture
- **Framework:** Spring Boot 3.2+ with Java 17
- **Database:** PostgreSQL 15+ with Flyway migrations
- **Authentication:** Stateless JWT with Spring Security 6
- **Caching:** Redis for query results and session data
- **API Docs:** OpenAPI 3.0 with Springdoc
- **Testing:** JUnit 5, Mockito, Testcontainers

### Frontend Architecture
- **Framework:** React 18+ with TypeScript 5.x
- **Build Tool:** Vite 5.x (fast HMR, optimized builds)
- **Styling:** Tailwind CSS + shadcn/ui components
- **State Management:** TanStack Query for server state, Context API for global state
- **Routing:** React Router v6
- **Form Handling:** React Hook Form + Zod validation
- **Charts:** Recharts for data visualization
- **Testing:** Vitest, React Testing Library, Playwright

### DevOps Strategy
- **Containerization:** Docker multi-stage builds
- **CI/CD:** GitHub Actions with automated testing
- **Frontend Hosting:** Vercel (CDN, automatic previews)
- **Backend Hosting:** Railway (PostgreSQL + Redis included)
- **Monitoring:** Spring Boot Actuator + Prometheus metrics
- **Security:** Snyk + OWASP Dependency Check

---

## 🗄️ Database Overview

**8 Core Tables:**
1. **users** - Authentication and user profiles
2. **households** - Expense sharing groups
3. **user_households** - Many-to-many with RBAC (OWNER/ADMIN/VIEWER)
4. **categories** - Hierarchical expense/income categories
5. **transactions** - Core financial transactions
6. **budgets** - Budget planning with rollover support
7. **budget_categories** - Link budgets to categories
8. **recurring_patterns** - AI-detected recurring transactions

**See:** [01_DATABASE_SCHEMA.md](./01_DATABASE_SCHEMA.md) for complete ER diagram and SQL DDL.

---

## 🌐 API Endpoints Summary

**36 REST Endpoints organized by domain:**

| Domain | Endpoints | Examples |
|--------|-----------|----------|
| **Authentication** | 4 | `POST /auth/register`, `POST /auth/login` |
| **Users** | 3 | `GET /users/me`, `PUT /users/me` |
| **Households** | 6 | `POST /households`, `GET /households/:id/members` |
| **Categories** | 4 | `GET /categories`, `POST /categories` |
| **Transactions** | 7 | `GET /transactions`, `POST /transactions`, `POST /transactions/bulk` |
| **Budgets** | 5 | `GET /budgets`, `POST /budgets`, `GET /budgets/:id/progress` |
| **Analytics** | 4 | `GET /analytics/dashboard`, `GET /analytics/trends` |
| **Recurring** | 3 | `GET /recurring-patterns` |

**Authentication:** Bearer JWT tokens  
**Authorization:** Role-based access control (RBAC)  
**Error Handling:** Standardized error responses with timestamps

**See:** [02_API_SPECIFICATION.md](./02_API_SPECIFICATION.md) for complete API documentation.

---

## 🧪 Testing Strategy

### Coverage Targets

| Test Type | Target | Tool |
|-----------|--------|------|
| Backend Unit Tests | ≥ 80% | JUnit 5 + Jacoco |
| Frontend Unit Tests | ≥ 75% | Vitest |
| Integration Tests | ≥ 70% | Spring Boot Test |
| E2E Tests | Critical flows | Playwright |
| Security Scan | 0 high vulnerabilities | Snyk + OWASP |

### Running Tests

```bash
# Backend tests
cd backend
mvn test                    # Unit tests
mvn verify                  # Integration tests
mvn jacoco:report          # Coverage report

# Frontend tests
cd frontend
npm run test:unit          # Unit tests
npm run test:e2e           # E2E tests (requires backend)
npm run test:coverage      # Coverage report

# Security scans
mvn dependency-check:check  # Backend
npm audit                   # Frontend
```

**See:** [04_TEST_STRATEGY.md](./04_TEST_STRATEGY.md) for complete testing guide.

---

## 🚀 Deployment

### Environments

| Environment | Backend | Frontend | Purpose |
|-------------|---------|----------|---------|
| **Development** | localhost:8080 | localhost:5173 | Local dev |
| **Staging** | Railway | Vercel Preview | Pre-prod testing |
| **Production** | Railway | Vercel | Live system |

### Deployment Commands

```bash
# Deploy to staging (auto on PR to develop)
git checkout develop
git push origin develop

# Deploy to production (manual approval)
git checkout main
git merge develop
git push origin main
```

### Deployment Checklist

**Before deploying to production:**
- [ ] All tests passing
- [ ] Code review approved
- [ ] Security scan passed
- [ ] Database migrations tested
- [ ] Rollback plan ready

**See:** [05_DEVOPS_PIPELINE.md](./05_DEVOPS_PIPELINE.md) for complete DevOps guide.

---

## 🔐 Security Features

### Authentication & Authorization
- ✓ JWT-based stateless authentication
- ✓ Password hashing with BCrypt (cost factor: 10)
- ✓ Role-based access control (RBAC)
- ✓ Token expiration and refresh mechanism

### Security Best Practices
- ✓ Parameterized SQL queries (JPA prevents injection)
- ✓ Input validation with Bean Validation
- ✓ XSS prevention with React's automatic escaping
- ✓ CSRF protection with SameSite cookies
- ✓ CORS configuration for trusted origins
- ✓ HTTPS-only in production
- ✓ Rate limiting (100 req/min per user)
- ✓ Secrets stored in environment variables

### Security Testing
- OWASP Top 10 vulnerability checks
- Dependency scanning with Snyk
- Manual penetration testing checklist

**See:** [04_TEST_STRATEGY.md](./04_TEST_STRATEGY.md#6-security-testing) for security test cases.

---

## 📊 Performance Targets

| Metric | Target | Measured By |
|--------|--------|-------------|
| API Response Time (p95) | < 500ms | Spring Boot Actuator |
| Database Query Time | < 100ms | Hibernate statistics |
| Frontend Bundle Size | < 500KB (gzipped) | Vite build analysis |
| Lighthouse Performance | ≥ 90 | Lighthouse CI |
| First Contentful Paint | < 1.5s | Lighthouse |
| Time to Interactive | < 3.5s | Lighthouse |

### Optimization Techniques
- Database connection pooling (HikariCP)
- Redis caching for frequently accessed data
- Database indexes on foreign keys and query columns
- Frontend code splitting and lazy loading
- Image optimization (WebP with fallback)
- Gzip compression for assets

---

## 🛠️ Development Workflow

### Git Branching Strategy

```
main (production)
  ├── develop (integration)
  │    ├── feature/user-authentication
  │    ├── feature/transaction-crud
  │    └── bugfix/date-validation
  └── hotfix/security-patch
```

### Commit Message Convention

```
feat: add recurring transaction detection
fix: resolve date range filter bug
docs: update API specification
test: add unit tests for budget service
chore: upgrade Spring Boot to 3.2.1
```

### Pull Request Process

1. Create feature branch from `develop`
2. Implement feature with tests
3. Push and create PR to `develop`
4. CI/CD runs automated checks
5. Request code review (≥1 approval required)
6. Merge after approval and passing checks
7. Delete feature branch

---

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
```bash
# Check PostgreSQL is running
docker ps | grep postgres

# Verify database connection
psql -h localhost -U postgres -d expense_tracker

# Check logs
tail -f backend/logs/expense-tracker.log
```

**Frontend can't connect to backend:**
```bash
# Verify backend is running
curl http://localhost:8080/actuator/health

# Check CORS configuration in backend
# Ensure frontend URL is in allowed origins

# Verify .env file
cat frontend/.env.development
```

**Database migration failed:**
```bash
# Check migration status
mvn flyway:info

# Validate migrations
mvn flyway:validate

# Repair migration history (if needed)
mvn flyway:repair
```

**Tests failing:**
```bash
# Clean and rebuild
mvn clean install -DskipTests
npm ci

# Run tests individually
mvn test -Dtest=TransactionServiceTest
npm run test:unit -- TransactionForm.test.tsx
```

---

## 📈 Monitoring & Observability

### Backend Monitoring

**Spring Boot Actuator Endpoints:**
- `/actuator/health` - Application health status
- `/actuator/metrics` - JVM and application metrics
- `/actuator/info` - Application information
- `/actuator/prometheus` - Prometheus metrics export

**Logs Location:**
- Development: `backend/logs/expense-tracker.log`
- Production: Stdout (Railway captures automatically)

### Frontend Monitoring

**Metrics to Track:**
- Lighthouse scores (Performance, Accessibility, SEO)
- Bundle size (track with `npm run build`)
- Error rate (integrate Sentry for production)

---

## 🤝 Contributing

### Code Style

**Backend (Java):**
- Follow Google Java Style Guide
- Run `mvn spotless:apply` before committing
- Max line length: 120 characters

**Frontend (TypeScript):**
- Follow Airbnb TypeScript Style Guide
- Run `npm run format` before committing
- Use Prettier for formatting
- Enable ESLint autofix in IDE

### Code Review Checklist

- [ ] Code follows project style guide
- [ ] Unit tests added/updated
- [ ] Documentation updated
- [ ] No console.log or debugging code
- [ ] No hardcoded credentials or secrets
- [ ] Error handling implemented
- [ ] Performance considerations addressed

---

## 📞 Support & Resources

### Documentation Links
- [Spring Boot Documentation](https://spring.io/projects/spring-boot)
- [React Documentation](https://react.dev/)
- [TanStack Query](https://tanstack.com/query/latest)
- [Tailwind CSS](https://tailwindcss.com/)
- [shadcn/ui](https://ui.shadcn.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Team Communication
- **Slack Channel:** #expense-tracker
- **Issue Tracker:** GitHub Issues
- **Wiki:** GitHub Wiki
- **Standup:** Daily at 10:00 AM

---

## 🗓️ Implementation Timeline

**Total Estimated Time:** 12-16 weeks

| Phase | Duration | Tasks |
|-------|----------|-------|
| **Phase 1: Foundation** | 2-3 weeks | Project setup, database schema, auth |
| **Phase 2: Backend APIs** | 3-4 weeks | REST endpoints, business logic |
| **Phase 3: Backend Testing** | 1 week | Unit + integration tests |
| **Phase 4: Frontend Core** | 2-3 weeks | Component library, routing, auth |
| **Phase 5: Frontend Features** | 2-3 weeks | Transaction UI, budgets, analytics |
| **Phase 6: Testing & Deployment** | 2 weeks | E2E tests, CI/CD, production deploy |

**See:** `Expense_Tracker.pdf` for detailed task breakdown (30 tasks total).

---

## ✅ Next Steps

1. **Review all documentation** in the `docs/` directory
2. **Set up local development environment** (see Quick Start above)
3. **Create GitHub repositories** (frontend + backend or monorepo)
4. **Initialize projects** with boilerplate code
5. **Start with Phase 1, Task 1** from the PDF implementation plan
6. **Follow the task sequence** for structured development

---

## 📝 License

**Proprietary** - All rights reserved  
© 2026 Expense Tracker Project

---

## 📄 Document Information

**Created:** August 4, 2026  
**Last Updated:** August 4, 2026  
**Version:** 1.0  
**Maintainers:** Project Team  

---

**Questions?** Review the detailed documentation or reach out to the team in #expense-tracker on Slack.
