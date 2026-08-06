# 💰 Expense Tracker

A full-stack web application for managing personal and household expenses with advanced budgeting, analytics, and multi-user support.

[![React](https://img.shields.io/badge/React-18.0+-61dafb?logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178c6?logo=typescript)](https://www.typescriptlang.org/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.2+-6db33f?logo=spring)](https://spring.io/projects/spring-boot)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?logo=postgresql)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Expense Tracker is a modern, secure, and feature-rich application designed to help individuals and households manage their finances effectively. Built with a robust Spring Boot backend and a responsive React frontend, it provides real-time insights into spending patterns, budget tracking, and financial analytics.

### Key Highlights

- 🔐 **Secure Authentication** - JWT-based authentication with BCrypt password hashing
- 👥 **Multi-User Support** - Household-based expense sharing and collaboration
- 📊 **Advanced Analytics** - Visual insights with charts and spending trends
- 💵 **Budget Tracking** - Create budgets with customizable alerts and rollover support
- 🏷️ **Smart Categorization** - Pre-defined and custom categories for better organization
- 🔍 **Powerful Filtering** - Search and filter transactions by date, category, amount, and tags
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- 🚀 **Real-time Updates** - Instant updates without page refresh

## ✨ Features

### Transaction Management
- ✅ Create, read, update, and delete transactions
- ✅ Support for both expenses and income
- ✅ Multiple payment methods (cash, credit card, debit card, etc.)
- ✅ Tag-based organization
- ✅ Bulk operations (delete multiple transactions)
- ✅ Advanced filtering and search
- ✅ Date range selection
- ✅ CSV and PDF export

### Budget Management
- ✅ Create budgets with custom time periods (weekly, monthly, yearly)
- ✅ Real-time progress tracking
- ✅ Customizable alert thresholds (e.g., alert at 80% spent)
- ✅ Color-coded status indicators
- ✅ Budget vs. actual spending comparison
- ✅ Rollover support for unused budget

### Analytics & Reporting
- ✅ Spending trends over time (line charts)
- ✅ Category-wise breakdown (pie charts)
- ✅ Month-over-month comparisons
- ✅ Income vs. expense analysis
- ✅ Top spending categories
- ✅ Predictive insights
- ✅ Custom date range reports

### Category Management
- ✅ Pre-defined categories (Food, Transport, Shopping, etc.)
- ✅ Custom category creation
- ✅ Category icons and colors
- ✅ Separate expense and income categories
- ✅ Category-based filtering

### User & Household Management
- ✅ User registration and login
- ✅ Profile management
- ✅ Household creation and management
- ✅ Role-based access control (Owner, Admin, Viewer)
- ✅ Multi-currency support

### Security
- ✅ JWT token-based authentication
- ✅ Password encryption with BCrypt
- ✅ Secure API endpoints
- ✅ CORS configuration
- ✅ Input validation and sanitization

## 🛠️ Tech Stack

### Frontend
- **Framework:** React 18.x
- **Language:** TypeScript 5.x
- **Build Tool:** Vite 8.x
- **Styling:** Tailwind CSS 3.x
- **State Management:** TanStack Query (React Query)
- **Routing:** React Router v6
- **Forms:** React Hook Form + Zod validation
- **Charts:** Recharts
- **UI Components:** shadcn/ui (Radix UI primitives)
- **Date Handling:** date-fns
- **Icons:** Lucide React
- **HTTP Client:** Axios

### Backend
- **Framework:** Spring Boot 3.2.x
- **Language:** Java 17+
- **Database:** PostgreSQL 15+
- **ORM:** Hibernate 6.x + Spring Data JPA
- **Security:** Spring Security 6.x + JWT (JJWT 0.12.x)
- **Migration:** Flyway 10.x
- **API Documentation:** Springdoc OpenAPI (Swagger)
- **Build Tool:** Maven 3.x
- **Testing:** JUnit 5, Mockito, Testcontainers

### DevOps & Tools
- **Containerization:** Docker & Docker Compose
- **Version Control:** Git
- **API Testing:** Postman / curl
- **Database Client:** pgAdmin / DBeaver
- **Development:** Hot reload (Vite HMR + Spring DevTools)

## 📸 Screenshots

> Add screenshots of your application here once the UI is complete

```
┌─────────────────────────────────────────────┐
│  📊 Dashboard                               │
│  - Summary cards (income, expenses, balance)│
│  - Recent transactions                      │
│  - Budget overview                          │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  💳 Transactions                            │
│  - Transaction list with filters            │
│  - Add/Edit transaction modal               │
│  - Bulk operations                          │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  🎯 Budgets                                 │
│  - Budget cards with progress bars          │
│  - Alert indicators                         │
│  - Budget creation form                     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  📈 Analytics                               │
│  - Spending trends (line chart)             │
│  - Category breakdown (pie chart)           │
│  - Period comparison                        │
└─────────────────────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18.x or higher ([Download](https://nodejs.org/))
- **Java** 17 or higher ([Download](https://adoptium.net/))
- **Maven** 3.8+ ([Download](https://maven.apache.org/))
- **Docker** and Docker Compose ([Download](https://www.docker.com/))
- **Git** ([Download](https://git-scm.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. **Start PostgreSQL database**
   ```bash
   docker compose up -d
   ```
   
   This will start PostgreSQL on port 5432 with:
   - Database: `expense_tracker`
   - Username: `postgres`
   - Password: `postgres`

3. **Start the Backend**
   ```bash
   cd backend
   
   # Set Java home (adjust path for your system)
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   
   # Run the application
   mvn spring-boot:run
   ```
   
   Backend will start on http://localhost:8080

4. **Start the Frontend**
   ```bash
   cd frontend
   
   # Install dependencies
   npm install
   
   # Start development server
   npm run dev
   ```
   
   Frontend will start on http://localhost:5173

5. **Access the application**
   
   Open your browser and navigate to: http://localhost:5173

### Default Test Account

A default test account is created on first run:

```
Email: john@example.com
Password: Test1234!
```

## 📚 API Documentation

### Base URL
```
http://localhost:8080/api/v1
```

### Authentication Endpoints

#### Register
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "fullName": "John Doe"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzUxMiJ9...",
  "type": "Bearer",
  "expiresIn": 86400,
  "user": {
    "id": 1,
    "email": "user@example.com",
    "fullName": "John Doe",
    "householdId": 1
  }
}
```

### Transaction Endpoints

All transaction endpoints require `Authorization: Bearer <token>` header.

#### Get All Transactions
```http
GET /households/{householdId}/transactions
```

**Query Parameters:**
- `startDate` (optional): Filter by start date (YYYY-MM-DD)
- `endDate` (optional): Filter by end date (YYYY-MM-DD)
- `type` (optional): EXPENSE or INCOME
- `categoryId` (optional): Filter by category
- `search` (optional): Search in description

#### Create Transaction
```http
POST /households/{householdId}/transactions
Content-Type: application/json

{
  "amount": 50.00,
  "type": "EXPENSE",
  "categoryId": 1,
  "description": "Grocery shopping",
  "transactionDate": "2026-08-05",
  "paymentMethod": "CREDIT_CARD",
  "tags": ["groceries", "food"]
}
```

#### Update Transaction
```http
PUT /households/{householdId}/transactions/{transactionId}
Content-Type: application/json

{
  "amount": 55.00,
  "description": "Grocery shopping (updated)"
}
```

#### Delete Transaction
```http
DELETE /households/{householdId}/transactions/{transactionId}
```

### Budget Endpoints

#### Get All Budgets
```http
GET /households/{householdId}/budgets
```

#### Create Budget
```http
POST /households/{householdId}/budgets
Content-Type: application/json

{
  "name": "Monthly Groceries",
  "amount": 500.00,
  "periodType": "MONTHLY",
  "startDate": "2026-08-01",
  "endDate": "2026-08-31",
  "alertThreshold": 80
}
```

### Category Endpoints

#### Get All Categories
```http
GET /households/{householdId}/categories
```

#### Create Category
```http
POST /households/{householdId}/categories
Content-Type: application/json

{
  "name": "Entertainment",
  "type": "EXPENSE",
  "icon": "🎬",
  "color": "#FF6B6B"
}
```

### Analytics Endpoints

#### Get Analytics Summary
```http
GET /households/{householdId}/analytics?startDate=2026-08-01&endDate=2026-08-31
```

**Response:**
```json
{
  "totalIncome": 3000.00,
  "totalExpenses": 2100.00,
  "balance": 900.00,
  "categoryBreakdown": [
    {
      "categoryName": "Food & Dining",
      "amount": 800.00,
      "percentage": 38.1
    }
  ],
  "dailyTrend": [...],
  "topCategories": [...]
}
```

For complete API documentation, run the backend and visit:
```
http://localhost:8080/swagger-ui.html
```

## 📁 Project Structure

```
expense-tracker/
├── backend/                    # Spring Boot backend
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/expensetracker/
│   │   │   │   ├── controller/      # REST API controllers
│   │   │   │   ├── service/         # Business logic
│   │   │   │   ├── repository/      # Data access layer
│   │   │   │   ├── model/           # Entity models
│   │   │   │   ├── dto/             # Data transfer objects
│   │   │   │   ├── security/        # JWT & security config
│   │   │   │   ├── config/          # Application config
│   │   │   │   └── exception/       # Exception handling
│   │   │   └── resources/
│   │   │       ├── application.yml  # App configuration
│   │   │       └── db/migration/    # Flyway migrations
│   │   └── test/                    # Unit & integration tests
│   ├── pom.xml                      # Maven dependencies
│   └── README.md
│
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── components/              # Reusable components
│   │   │   ├── ui/                  # shadcn/ui components
│   │   │   ├── layout/              # Layout components
│   │   │   └── features/            # Feature-specific components
│   │   ├── pages/                   # Page components
│   │   │   ├── auth/                # Login, Register
│   │   │   ├── dashboard/           # Dashboard
│   │   │   ├── transactions/        # Transactions page
│   │   │   ├── budgets/             # Budgets page
│   │   │   └── analytics/           # Analytics page
│   │   ├── api/                     # API client & services
│   │   ├── contexts/                # React contexts
│   │   ├── hooks/                   # Custom React hooks
│   │   ├── types/                   # TypeScript types
│   │   ├── utils/                   # Utility functions
│   │   ├── App.tsx                  # Root component
│   │   └── main.tsx                 # Entry point
│   ├── public/                      # Static assets
│   ├── package.json                 # npm dependencies
│   ├── vite.config.ts               # Vite configuration
│   ├── tailwind.config.js           # Tailwind CSS config
│   ├── tsconfig.json                # TypeScript config
│   └── README.md
│
├── docs/                       # Documentation
│   ├── 01_DATABASE_SCHEMA.md
│   ├── 02_API_SPECIFICATION.md
│   ├── 03_ARCHITECTURE_DIAGRAMS.md
│   ├── 04_TEST_STRATEGY.md
│   └── 05_DEVOPS_PIPELINE.md
│
├── docker-compose.yml          # Docker Compose config
├── .gitignore                  # Git ignore rules
├── LICENSE                     # License file
└── README.md                   # This file
```

## 💻 Development

### Backend Development

#### Running Tests
```bash
cd backend
mvn test
```

#### Build JAR
```bash
mvn clean package
```

#### Database Migrations

Flyway handles database migrations automatically. To create a new migration:

1. Create a new file in `src/main/resources/db/migration/`
2. Name it: `V{version}__Description.sql` (e.g., `V2__Add_recurring_transactions.sql`)
3. Write your SQL
4. Restart the application

#### View Database
```bash
# Connect to PostgreSQL
docker exec -it expense-tracker-db psql -U postgres -d expense_tracker

# List tables
\dt

# View table structure
\d+ users
```

### Frontend Development

#### Install Additional Dependencies
```bash
cd frontend

# State management
npm install @tanstack/react-query

# Routing
npm install react-router-dom

# Forms
npm install react-hook-form zod @hookform/resolvers

# Charts
npm install recharts

# Utilities
npm install date-fns lucide-react
```

#### Build for Production
```bash
npm run build
```

#### Preview Production Build
```bash
npm run preview
```

#### Linting
```bash
npm run lint
```

### Environment Variables

#### Backend (`application.yml`)
```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/expense_tracker
    username: postgres
    password: postgres

jwt:
  secret: your-secret-key-change-in-production
  expiration: 86400000  # 24 hours
```

#### Frontend (`.env`)
```env
VITE_API_BASE_URL=http://localhost:8080/api/v1
```

## 🧪 Testing

### Backend Testing

```bash
cd backend

# Run all tests
mvn test

# Run specific test class
mvn test -Dtest=TransactionServiceTest

# Run with coverage
mvn test jacoco:report
```

### Frontend Testing

```bash
cd frontend

# Install test dependencies
npm install --save-dev vitest @testing-library/react @testing-library/jest-dom

# Run tests
npm test

# Run tests with coverage
npm run test:coverage
```

### Integration Testing

```bash
# Use Postman collection (import from docs/)
# Or use curl scripts

# Test complete flow
curl -X POST http://localhost:8080/api/v1/auth/register -H "Content-Type: application/json" -d '{"email":"test@example.com","password":"Test123!","fullName":"Test User"}'
```

## 🚢 Deployment

### Using Docker

#### Build Docker Images
```bash
# Backend
cd backend
docker build -t expense-tracker-backend .

# Frontend
cd frontend
docker build -t expense-tracker-frontend .
```

#### Run with Docker Compose
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Deploy to Cloud

#### Backend (Railway, Heroku, AWS)
1. Set environment variables
2. Configure PostgreSQL connection
3. Deploy JAR file
4. Run Flyway migrations

#### Frontend (Vercel, Netlify, AWS S3)
1. Build production bundle: `npm run build`
2. Deploy `dist` folder
3. Configure environment variables
4. Set up routing (SPA fallback)

### Production Checklist

- [ ] Change JWT secret key
- [ ] Update CORS origins
- [ ] Use production database
- [ ] Enable HTTPS
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Set up CI/CD pipeline
- [ ] Add rate limiting
- [ ] Configure error tracking (Sentry)
- [ ] Set up logging (CloudWatch, Datadog)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards

- **Java:** Follow Google Java Style Guide
- **TypeScript/React:** Follow Airbnb React Style Guide
- **Commits:** Use conventional commits (feat, fix, docs, etc.)
- **Tests:** Write tests for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Spring Boot](https://spring.io/projects/spring-boot) - Backend framework
- [React](https://reactjs.org/) - Frontend library
- [Tailwind CSS](https://tailwindcss.com/) - CSS framework
- [shadcn/ui](https://ui.shadcn.com/) - UI components
- [Recharts](https://recharts.org/) - Charting library
- [PostgreSQL](https://www.postgresql.org/) - Database

## 📞 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - your.email@example.com

Project Link: [https://github.com/yourusername/expense-tracker](https://github.com/yourusername/expense-tracker)

---

## 🗺️ Roadmap

### Phase 1: Foundation ✅
- [x] Project setup
- [x] Database schema
- [x] Authentication system
- [x] Basic CRUD operations

### Phase 2: Core Features ✅
- [x] Transaction management
- [x] Budget tracking
- [x] Category management
- [x] Analytics backend

### Phase 3: Frontend (In Progress) ⏳
- [ ] Login/Register UI
- [ ] Dashboard with charts
- [ ] Transaction management UI
- [ ] Budget tracking UI
- [ ] Analytics visualization

### Phase 4: Advanced Features (Planned) 📋
- [ ] Recurring transactions
- [ ] Receipt upload & OCR
- [ ] Bill reminders
- [ ] Expense splitting
- [ ] Multi-household support
- [ ] Mobile app (React Native)
- [ ] Export to QuickBooks/Xero
- [ ] Email notifications
- [ ] Custom reports
- [ ] AI-powered insights

### Phase 5: Polish & Launch 🚀
- [ ] Comprehensive testing
- [ ] Performance optimization
- [ ] Security audit
- [ ] Documentation
- [ ] Production deployment

---

**Made with ❤️ using Spring Boot and React**
