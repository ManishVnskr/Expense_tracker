# 💰 Expense Tracker

> A modern, full-stack expense tracking application with budget management and analytics

[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.2.1-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Expense Tracker is a production-ready web application that helps users manage their personal finances effectively. It provides comprehensive tools for tracking transactions, setting budgets, and gaining insights through interactive analytics.

Built with **Spring Boot** and **React**, this application demonstrates modern full-stack development practices including:
- RESTful API design
- JWT-based authentication
- Type-safe frontend with TypeScript
- Responsive design with Tailwind CSS
- Database migrations with Flyway
- Containerized development with Docker

## ✨ Features

### 🔐 Authentication & Security
- Secure user registration and login
- JWT token-based authentication
- Password hashing with BCrypt
- Protected API endpoints

### 💳 Transaction Management
- **Create, read, update, and delete** transactions
- Support for both expenses and income
- **Advanced filtering** by date range, category, and type
- **Search functionality** by description
- **Bulk delete** multiple transactions
- Tag support for better organization
- Multiple payment methods (Cash, Credit Card, Debit Card, UPI, etc.)

### 💰 Budget Tracking
- Create custom budgets with specific periods (weekly, monthly, yearly)
- **Visual progress bars** with color-coded status
  - ✅ Green: Under 80% of budget
  - ⚠️ Yellow: 80-100% of budget
  - 🔴 Red: Over budget
- Alert threshold customization
- Budget rollover support
- Real-time budget status updates

### 📊 Analytics & Insights
- **Dashboard overview** with key metrics
  - Total income, expenses, and balance
  - Pie chart of expenses by category
  - Recent transactions preview
  - Active budgets summary
- **Analytics page** with detailed visualizations
  - Line chart: Income vs Expenses over time
  - Bar chart: Top spending categories
  - Period selector (3, 6, 12 months)
  - Automated spending insights

### 📱 User Experience
- **Responsive design** - works on desktop, tablet, and mobile
- **Auto-refresh** functionality for real-time updates
- Clean, modern UI with Tailwind CSS
- Intuitive navigation and user flows
- Form validation with helpful error messages

## 🛠 Tech Stack

### Backend
- **Framework:** Spring Boot 3.2.1
- **Language:** Java 17
- **Database:** PostgreSQL 15
- **ORM:** Hibernate + Spring Data JPA
- **Migration:** Flyway
- **Security:** Spring Security 6 + JWT (JJWT 0.12.3)
- **Build Tool:** Maven
- **API Documentation:** REST principles

### Frontend
- **Framework:** React 18
- **Language:** TypeScript 5
- **Build Tool:** Vite 8.2
- **Styling:** Tailwind CSS 4
- **Data Fetching:** TanStack Query v5
- **Routing:** React Router v7
- **Forms:** React Hook Form + Zod validation
- **Charts:** Recharts
- **HTTP Client:** Axios

### DevOps
- **Containerization:** Docker Compose
- **Database:** PostgreSQL container
- **Development:** Hot reload for both frontend and backend

## 📸 Screenshots

### Dashboard
![Dashboard](docs/screenshots/dashboard.png)
*Overview with expense summary and visualizations*

### Transactions
![Transactions](docs/screenshots/transactions.png)
*Full transaction management with filtering and search*

### Budgets
![Budgets](docs/screenshots/budgets.png)
*Budget tracking with progress indicators*

### Analytics
![Analytics](docs/screenshots/analytics.png)
*Detailed analytics with interactive charts*

## 🚀 Getting Started

### Prerequisites

- **Java 17+** ([Download](https://adoptium.net/))
- **Node.js 18+** ([Download](https://nodejs.org/))
- **Docker & Docker Compose** ([Download](https://www.docker.com/))
- **Maven 3.9+** (usually bundled with IDEs)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. **Start PostgreSQL**
   ```bash
   docker compose up -d
   ```

3. **Start the Backend**
   ```bash
   cd backend
   mvn spring-boot:run
   ```
   Backend will run on http://localhost:8080

4. **Start the Frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Frontend will run on http://localhost:5173

5. **Access the Application**
   - Open http://localhost:5173 in your browser
   - Register a new account or use test credentials:
     ```
     Email: john@example.com
     Password: Test1234!
     ```

### Quick Commands

```bash
# Start all services
docker compose up -d                    # Database
cd backend && mvn spring-boot:run       # Backend (separate terminal)
cd frontend && npm run dev              # Frontend (separate terminal)

# Stop services
docker compose down                     # Database
# Use Ctrl+C to stop backend/frontend
```

## 📁 Project Structure

```
expense-tracker/
├── backend/                           # Spring Boot backend
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/expensetracker/
│   │   │   │   ├── controller/       # REST API endpoints
│   │   │   │   ├── service/          # Business logic
│   │   │   │   ├── repository/       # Data access layer
│   │   │   │   ├── model/            # JPA entities
│   │   │   │   ├── dto/              # Data transfer objects
│   │   │   │   ├── security/         # JWT authentication
│   │   │   │   ├── config/           # Spring configuration
│   │   │   │   └── exception/        # Error handling
│   │   │   └── resources/
│   │   │       ├── application.yml   # App configuration
│   │   │       └── db/migration/     # Flyway SQL scripts
│   │   └── test/                     # Unit & integration tests
│   └── pom.xml                       # Maven dependencies
│
├── frontend/                          # React frontend
│   ├── src/
│   │   ├── components/               # React components
│   │   ├── pages/                    # Page components
│   │   ├── api/                      # API client functions
│   │   ├── contexts/                 # React contexts
│   │   ├── hooks/                    # Custom React hooks
│   │   ├── types/                    # TypeScript types
│   │   ├── utils/                    # Utility functions
│   │   ├── App.tsx                   # Main app component
│   │   └── main.tsx                  # Entry point
│   ├── package.json                  # NPM dependencies
│   ├── vite.config.ts                # Vite configuration
│   └── tailwind.config.js            # Tailwind CSS config
│
├── docs/                              # Documentation
│   ├── 01_DATABASE_SCHEMA.md         # Database design
│   ├── 02_API_SPECIFICATION.md       # API endpoints
│   ├── 03_ARCHITECTURE_DIAGRAMS.md   # System architecture
│   ├── 04_TEST_STRATEGY.md           # Testing approach
│   └── 05_DEVOPS_PIPELINE.md         # Deployment guide
│
├── docker-compose.yml                 # Docker services
├── LICENSE                            # MIT license
└── README.md                          # This file
```

## 📚 API Documentation

### Base URL
```
http://localhost:8080/api/v1
```

### Authentication

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

### Transactions

#### Get All Transactions
```http
GET /households/{householdId}/transactions
Authorization: Bearer {token}

Query Parameters:
- startDate (optional): YYYY-MM-DD
- endDate (optional): YYYY-MM-DD
- categoryId (optional): number
- type (optional): EXPENSE | INCOME
- search (optional): string
```

#### Create Transaction
```http
POST /households/{householdId}/transactions
Authorization: Bearer {token}
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
PUT /households/{householdId}/transactions/{id}
Authorization: Bearer {token}
Content-Type: application/json

{
  "amount": 55.00,
  "description": "Updated description"
}
```

#### Delete Transaction
```http
DELETE /households/{householdId}/transactions/{id}
Authorization: Bearer {token}
```

### Budgets

#### Get All Budgets
```http
GET /households/{householdId}/budgets
Authorization: Bearer {token}
```

#### Create Budget
```http
POST /households/{householdId}/budgets
Authorization: Bearer {token}
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

### Analytics

#### Get Analytics Summary
```http
GET /households/{householdId}/analytics?startDate=2026-08-01&endDate=2026-08-31
Authorization: Bearer {token}
```

**Response:**
```json
{
  "totalIncome": 5000.00,
  "totalExpenses": 3500.00,
  "balance": 1500.00,
  "categoryBreakdown": [
    {"categoryId": 1, "categoryName": "Groceries", "amount": 800.00},
    {"categoryId": 2, "categoryName": "Transport", "amount": 500.00}
  ],
  "monthlyTrends": [
    {"month": "2026-08", "income": 5000.00, "expenses": 3500.00}
  ],
  "topCategories": [...]
}
```

For complete API documentation, see [API_SPECIFICATION.md](docs/02_API_SPECIFICATION.md)

## 🔧 Development

### Database Schema

The application uses 5 main tables:

- **users** - User accounts
- **households** - User groupings (for shared expenses)
- **categories** - Expense/income categories
- **transactions** - Financial transactions
- **budgets** - Budget definitions

See [DATABASE_SCHEMA.md](docs/01_DATABASE_SCHEMA.md) for detailed schema.

### Database Migrations

Migrations are managed by Flyway and run automatically on startup:

```sql
-- Location: backend/src/main/resources/db/migration/
V1__Initial_Schema.sql  -- Create tables
V2__Seed_Data.sql       -- Insert default categories
```

### Environment Variables

#### Backend (`backend/src/main/resources/application.yml`)
```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/expense_tracker
    username: postgres
    password: postgres
  
jwt:
  secret: your-secret-key-min-256-bits
  expiration: 86400000  # 24 hours
```

#### Frontend (`frontend/.env`)
```bash
VITE_API_BASE_URL=http://localhost:8080/api/v1
```

### Running Tests

```bash
# Backend tests (JUnit)
cd backend
mvn test

# Frontend tests (Vitest)
cd frontend
npm test
```

### Code Quality

```bash
# Frontend linting
cd frontend
npm run lint
```

## 🚢 Deployment

### Docker Production Build

```bash
# Build backend
cd backend
mvn clean package -DskipTests

# Build frontend
cd frontend
npm run build

# Use production Docker Compose (create this file)
docker compose -f docker-compose.prod.yml up -d
```

### Platform Recommendations

- **Backend:** Railway, Render, Heroku
- **Frontend:** Vercel, Netlify, Cloudflare Pages
- **Database:** Railway PostgreSQL, Supabase, Amazon RDS

For detailed deployment guide, see [DEVOPS_PIPELINE.md](docs/05_DEVOPS_PIPELINE.md)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow existing code style and conventions
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGithub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Spring Boot team for the excellent framework
- React team for the modern frontend library
- Tailwind CSS for the utility-first styling
- TanStack Query for data fetching solution
- All open-source contributors

## 📞 Support

For support, email support@example.com or open an issue in the GitHub repository.

---

**⭐ If you find this project helpful, please consider giving it a star!**

---

## 📈 Project Status

- ✅ **Version 1.0** - MVP Complete (August 2026)
  - All core features implemented
  - Backend API fully functional
  - Frontend UI complete
  - Docker development setup
  - Comprehensive documentation

### Roadmap

**v1.1 - Enhanced Features**
- [ ] Email notifications for budget alerts
- [ ] Recurring transaction detection
- [ ] Export to CSV/PDF
- [ ] Multi-currency support

**v1.2 - Collaboration**
- [ ] Household member management
- [ ] Shared expense splitting
- [ ] Role-based access control (Owner/Admin/Viewer)

**v2.0 - Advanced Analytics**
- [ ] AI-powered spending predictions
- [ ] Custom report builder
- [ ] Mobile app (React Native)
- [ ] Bank account integration

## 🔗 Links

- [Demo](https://expense-tracker-demo.vercel.app) *(coming soon)*
- [Documentation](docs/README.md)
- [API Specification](docs/02_API_SPECIFICATION.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

---

Made with ❤️ using Spring Boot and React
