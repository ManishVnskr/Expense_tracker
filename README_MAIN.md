# Expense Tracker - Full Stack Application

**Status:** 9/14 Tasks Complete (64%)  
**Time:** Day 1, 3:25 PM  
**Demo Target:** Day 2 Evening

---

## 🚀 Quick Start

### Prerequisites
- Java 17
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL (or use Docker)

### Running the Application

```bash
# 1. Start PostgreSQL
docker compose up -d

# 2. Start Backend (Terminal 1)
cd backend
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 mvn spring-boot:run

# 3. Start Frontend (Terminal 2)
cd frontend
npm install  # first time only
npm run dev

# Access the app
# Frontend: http://localhost:5173
# Backend API: http://localhost:8080
```

---

## ✅ What's Working

### Backend API (100% Complete)
- ✅ JWT Authentication (register, login)
- ✅ User profile with auto-created household
- ✅ 15 default categories (Food, Transport, etc.)
- ✅ Transaction CRUD with filtering, search, bulk delete
- ✅ Budget tracking with alerts (OK/WARNING/EXCEEDED)
- ✅ Analytics dashboard (expenses, income, balance, charts)
- ✅ Trends API (6-month comparison)

**API Base:** http://localhost:8080/api/v1

### Frontend (64% Complete)
- ✅ React 18 + TypeScript + Vite
- ✅ Tailwind CSS styling
- ✅ Login & Registration pages
- ✅ Protected routes with JWT
- ✅ Navigation layout
- ✅ API client with interceptors
- ⏳ Transaction management UI (next)
- ⏳ Budget UI with progress bars
- ⏳ Dashboard with charts
- ⏳ Analytics page

---

## 📁 Project Structure

```
expense-tracker/
├── backend/                  # Spring Boot 3.2 + Java 17
│   ├── src/main/java/
│   │   └── com/expensetracker/
│   │       ├── controller/   # REST endpoints
│   │       ├── service/      # Business logic
│   │       ├── repository/   # Data access
│   │       ├── model/        # JPA entities
│   │       ├── security/     # JWT & Spring Security
│   │       └── dto/          # Request/Response objects
│   ├── src/main/resources/
│   │   ├── application.yml
│   │   └── db/migration/     # Flyway SQL scripts
│   └── pom.xml
│
├── frontend/                 # React 18 + TypeScript
│   ├── src/
│   │   ├── api/             # API client & functions
│   │   ├── components/      # Reusable components
│   │   ├── contexts/        # React contexts (Auth)
│   │   ├── pages/           # Route pages
│   │   ├── types/           # TypeScript interfaces
│   │   └── utils/           # Helper functions
│   ├── package.json
│   └── tailwind.config.js
│
├── docker-compose.yml        # PostgreSQL container
├── CONTINUE_GUIDE.md        # Next steps guide
└── IMPLEMENTATION_STATUS.md  # Detailed status
```

---

## 🗄️ Database Schema

**5 Tables:**
1. `users` - Authentication & profiles
2. `households` - Expense groups (one per user for MVP)
3. `categories` - Expense/Income categories (15 defaults + custom)
4. `transactions` - Financial transactions with filtering
5. `budgets` - Budget tracking with alert thresholds

**Migrations:** Flyway manages schema (see `backend/src/main/resources/db/migration/`)

---

## 🔑 API Endpoints (20 total)

### Authentication
- `POST /api/v1/auth/register` - Create account
- `POST /api/v1/auth/login` - Get JWT token
- `GET /api/v1/users/me` - Get current user

### Categories
- `GET /api/v1/households/{id}/categories` - List categories
- `POST /api/v1/households/{id}/categories` - Create category
- `DELETE /api/v1/households/{id}/categories/{cid}` - Delete

### Transactions
- `GET /api/v1/households/{id}/transactions` - List with filters
- `POST /api/v1/households/{id}/transactions` - Create
- `PUT /api/v1/households/{id}/transactions/{tid}` - Update
- `DELETE /api/v1/households/{id}/transactions/{tid}` - Delete
- `DELETE /api/v1/households/{id}/transactions/bulk` - Bulk delete

### Budgets
- `GET /api/v1/households/{id}/budgets` - List with progress
- `POST /api/v1/households/{id}/budgets` - Create
- `PUT /api/v1/households/{id}/budgets/{bid}` - Update
- `DELETE /api/v1/households/{id}/budgets/{bid}` - Delete
- `GET /api/v1/households/{id}/budgets/{bid}` - Get progress

### Analytics
- `GET /api/v1/households/{id}/analytics/dashboard` - Summary data
- `GET /api/v1/households/{id}/analytics/trends?months=6` - Trends

---

## 🧪 Testing

### Test Backend API
```bash
# Register user
curl -X POST http://localhost:8080/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"Test1234!","fullName":"Test User"}'

# Login
curl -X POST http://localhost:8080/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"Test1234!"}'

# Use the token from login response
TOKEN="your_jwt_token_here"

# Get categories
curl http://localhost:8080/api/v1/households/1/categories \
  -H "Authorization: Bearer $TOKEN"

# Create transaction
curl -X POST http://localhost:8080/api/v1/households/1/transactions \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 50.00,
    "type": "EXPENSE",
    "categoryId": 1,
    "description": "Lunch",
    "transactionDate": "2026-08-05"
  }'
```

### Test Frontend
1. Open http://localhost:5173
2. Click "Register here"
3. Fill form: test@example.com / Test1234! / Test User
4. You'll be logged in automatically
5. Navigate using top menu

---

## 🛠️ Technology Stack

### Backend
- Spring Boot 3.2.1
- Spring Security 6 (JWT)
- Spring Data JPA
- PostgreSQL 15
- Flyway migrations
- Lombok
- Maven

### Frontend
- React 18
- TypeScript 5
- Vite 5
- Tailwind CSS 3
- TanStack Query v5
- React Router v6
- Axios
- Recharts
- React Hook Form + Zod

### DevOps
- Docker & Docker Compose
- PostgreSQL in container

---

## 📝 Next Steps

**See `CONTINUE_GUIDE.md` for detailed implementation steps.**

### Remaining Tasks (5 total):
1. **Task 10:** Transaction Management UI (table, filters, CRUD)
2. **Task 11:** Budget UI (cards, progress bars, alerts)
3. **Task 12:** Dashboard (summary cards, pie chart, widgets)
4. **Task 13:** Analytics (line/bar charts, trends)
5. **Task 14:** Polish (categories page, loading states, responsive)

**Estimated Time:** 14-16 hours remaining

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check PostgreSQL
docker ps | grep postgres

# Verify Java version
java -version  # Should be 17

# View logs
tail -f backend/backend.log
```

### Frontend errors
```bash
# Verify backend is running
curl http://localhost:8080/actuator/health

# Check .env file
cat frontend/.env  # Should have VITE_API_BASE_URL

# Reinstall dependencies
cd frontend && rm -rf node_modules && npm install
```

### Database connection issues
```bash
# Restart PostgreSQL
docker compose down
docker compose up -d

# Verify connection
docker exec -it expense-tracker-db psql -U postgres -d expense_tracker -c "\dt"
```

---

## 📊 Progress Tracking

- [x] Backend API (7/7 tasks)
- [x] Frontend Auth (2/2 tasks)
- [ ] Frontend Features (5/5 tasks)

**Current:** 9/14 tasks (64%)  
**Target:** 14/14 tasks by Day 2 evening

---

## 👤 Author

Built during 2-day MVP sprint (August 5-6, 2026)

---

## 📄 License

Proprietary - All rights reserved
