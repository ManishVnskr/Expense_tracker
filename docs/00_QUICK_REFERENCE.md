# Quick Reference Guide - Expense Tracker

## 🚀 Essential Commands

### Development

```bash
# Backend
cd backend
mvn spring-boot:run                # Start backend (port 8080)
mvn test                           # Run unit tests
mvn verify                         # Run all tests
mvn flyway:migrate                 # Run DB migrations

# Frontend
cd frontend
npm run dev                        # Start dev server (port 5173)
npm run test:unit                  # Run unit tests
npm run test:e2e                   # Run E2E tests
npm run build                      # Production build

# Docker
docker-compose up -d               # Start all services
docker-compose down                # Stop all services
docker-compose logs -f backend     # View logs
```

---

## 📦 Tech Stack at a Glance

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18 + TypeScript + Vite + TailwindCSS + shadcn/ui |
| **Backend** | Spring Boot 3.2 + Java 17 + Spring Security + JWT |
| **Database** | PostgreSQL 15 + Flyway migrations |
| **Cache** | Redis 7 |
| **Testing** | JUnit 5, Mockito, Testcontainers, Vitest, Playwright |
| **Deployment** | Vercel (frontend) + Railway (backend) + GitHub Actions |

---

## 🗄️ Database Tables

1. `users` - User authentication
2. `households` - Expense groups
3. `user_households` - RBAC membership
4. `categories` - Expense categories
5. `transactions` - Financial transactions
6. `budgets` - Budget planning
7. `budget_categories` - Budget allocations
8. `recurring_patterns` - AI-detected patterns

---

## 🌐 API Endpoints (36 total)

```
Authentication:
  POST   /api/v1/auth/register
  POST   /api/v1/auth/login
  POST   /api/v1/auth/refresh
  POST   /api/v1/auth/logout

Users:
  GET    /api/v1/users/me
  PUT    /api/v1/users/me
  POST   /api/v1/users/me/change-password

Households:
  GET    /api/v1/households
  POST   /api/v1/households
  GET    /api/v1/households/{id}
  POST   /api/v1/households/{id}/members
  PATCH  /api/v1/households/{id}/members/{userId}
  DELETE /api/v1/households/{id}/members/{userId}

Transactions:
  GET    /api/v1/households/{id}/transactions
  POST   /api/v1/households/{id}/transactions
  PUT    /api/v1/households/{id}/transactions/{tid}
  DELETE /api/v1/households/{id}/transactions/{tid}
  POST   /api/v1/households/{id}/transactions/bulk

Budgets:
  GET    /api/v1/households/{id}/budgets
  POST   /api/v1/households/{id}/budgets
  PUT    /api/v1/households/{id}/budgets/{bid}
  DELETE /api/v1/households/{id}/budgets/{bid}
  GET    /api/v1/households/{id}/budgets/{bid}/progress

Analytics:
  GET    /api/v1/households/{id}/analytics/dashboard
  GET    /api/v1/households/{id}/analytics/trends
  GET    /api/v1/households/{id}/analytics/categories
  GET    /api/v1/households/{id}/analytics/predictions
```

---

## 🧪 Testing Targets

| Test Type | Coverage | Tool |
|-----------|----------|------|
| Backend Unit | ≥ 80% | JUnit 5 + Jacoco |
| Frontend Unit | ≥ 75% | Vitest |
| Integration | ≥ 70% | Testcontainers |
| E2E | Critical flows | Playwright |
| Security | 0 high CVEs | Snyk + OWASP |

---

## 🔐 Environment Variables

### Backend (application.yml)
```yaml
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/expense_tracker
SPRING_DATASOURCE_USERNAME=postgres
SPRING_DATASOURCE_PASSWORD=postgres
JWT_SECRET=your-256-bit-secret-key-here
SPRING_REDIS_HOST=localhost
SPRING_REDIS_PORT=6379
```

### Frontend (.env)
```bash
VITE_API_BASE_URL=http://localhost:8080/api/v1
VITE_ENV=development
```

---

## 🚦 CI/CD Pipeline

```
Push → Lint → Build → Test → Security Scan → Deploy
```

**Triggers:**
- PR to `develop` → Deploy to Staging
- Push to `main` → Deploy to Production (manual approval)

**Status Checks:**
- ✓ ESLint / Checkstyle
- ✓ TypeScript / Java compilation
- ✓ Unit tests (≥80% coverage)
- ✓ Integration tests
- ✓ Security scan (Snyk)

---

## 📊 Performance Targets

| Metric | Target |
|--------|--------|
| API Response (p95) | < 500ms |
| Database Query | < 100ms |
| Frontend Bundle | < 500KB gzipped |
| Lighthouse Score | ≥ 90 |
| First Contentful Paint | < 1.5s |

---

## 🐛 Quick Troubleshooting

**Backend won't start:**
```bash
# Check DB connection
docker ps | grep postgres
psql -h localhost -U postgres -d expense_tracker

# View logs
tail -f backend/logs/expense-tracker.log
```

**Frontend API errors:**
```bash
# Verify backend is up
curl http://localhost:8080/actuator/health

# Check CORS settings
# Ensure VITE_API_BASE_URL is correct in .env
```

**Migration failed:**
```bash
mvn flyway:info      # Check status
mvn flyway:validate  # Validate migrations
mvn flyway:repair    # Fix checksums (dev only)
```

**Tests failing:**
```bash
# Clean rebuild
mvn clean install -DskipTests
npm ci

# Run specific test
mvn test -Dtest=TransactionServiceTest
```

---

## 📁 Project Structure

```
expense-tracker/
├── backend/
│   ├── src/main/java/com/expensetracker/
│   │   ├── controller/     # REST endpoints
│   │   ├── service/        # Business logic
│   │   ├── repository/     # Data access
│   │   ├── model/          # Entities + DTOs
│   │   └── security/       # JWT auth
│   └── src/main/resources/
│       └── db/migration/   # Flyway scripts
│
├── frontend/
│   └── src/
│       ├── components/     # React components
│       ├── pages/          # Route pages
│       ├── api/            # API client
│       ├── hooks/          # Custom hooks
│       └── types/          # TypeScript types
│
├── docs/                   # Documentation
└── .github/workflows/      # CI/CD
```

---

## 🔑 RBAC Permissions

| Role | View | Create | Edit | Delete | Manage Members |
|------|------|--------|------|--------|----------------|
| **OWNER** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **ADMIN** | ✓ | ✓ | ✓ | ✓ | ✗ |
| **VIEWER** | ✓ | ✗ | ✗ | ✗ | ✗ |

---

## 📚 Documentation Links

| Doc | Purpose |
|-----|---------|
| [README.md](./README.md) | Project overview & setup |
| [01_DATABASE_SCHEMA.md](./01_DATABASE_SCHEMA.md) | DB design + SQL DDL |
| [02_API_SPECIFICATION.md](./02_API_SPECIFICATION.md) | REST API docs |
| [03_ARCHITECTURE_DIAGRAMS.md](./03_ARCHITECTURE_DIAGRAMS.md) | System architecture |
| [04_TEST_STRATEGY.md](./04_TEST_STRATEGY.md) | Testing guide |
| [05_DEVOPS_PIPELINE.md](./05_DEVOPS_PIPELINE.md) | CI/CD + deployment |

---

## 🗓️ Timeline: 12-16 Weeks

| Phase | Duration | Key Deliverables |
|-------|----------|------------------|
| 1. Foundation | 2-3 weeks | DB schema, auth, basic CRUD |
| 2. Backend APIs | 3-4 weeks | All 36 endpoints + tests |
| 3. Backend Testing | 1 week | 80%+ coverage achieved |
| 4. Frontend Core | 2-3 weeks | Components, routing, auth |
| 5. Frontend Features | 2-3 weeks | Transactions, budgets, analytics |
| 6. Testing & Deploy | 2 weeks | E2E tests, CI/CD, launch |

---

## ✅ Definition of Done

- [ ] Unit tests pass (≥80% coverage)
- [ ] Integration tests pass
- [ ] Code review approved (≥1 approval)
- [ ] Security scan clean (no high CVEs)
- [ ] Documentation updated
- [ ] Deployed to staging successfully
- [ ] Manual QA testing completed

---

**Version:** 1.0 | **Last Updated:** August 4, 2026
