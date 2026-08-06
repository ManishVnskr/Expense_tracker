# 🚀 Quick Start Guide

## ✅ Status: ALL SYSTEMS RUNNING!

**Date:** August 5, 2026  
**Services:** 3/3 Running

---

## 🌐 Access Your Application

### Frontend Application
**URL:** http://localhost:5173

### Backend API
**URL:** http://localhost:8080/api/v1

### Test Account
```
Email:    john@example.com
Password: Test1234!
```

---

## 🎯 Quick Test

### 1. Open Frontend
```bash
open http://localhost:5173
# Or visit in your browser
```

### 2. Test Backend API
```bash
# Login
curl -X POST http://localhost:8080/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"Test1234!"}'

# Response includes JWT token and user info
```

---

## 🛠️ Server Management

### View Running Services
```bash
# Check all services
cd /home/govind/Desktop/project

# PostgreSQL
docker ps | grep expense-tracker-db

# Backend
ps aux | grep spring-boot:run | grep -v grep

# Frontend
ps aux | grep vite | grep -v grep
```

### Stop Services
```bash
# Stop Backend
kill $(cat backend/backend.pid)

# Stop Frontend
kill $(cat frontend/frontend.pid)

# Stop PostgreSQL
docker compose down
```

### Start Services (if stopped)
```bash
# 1. PostgreSQL
docker compose up -d

# 2. Backend (wait 5s after PostgreSQL)
cd backend
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 \
  nohup mvn spring-boot:run > backend.log 2>&1 & echo $! > backend.pid

# 3. Frontend (wait 15s for backend)
cd ../frontend
nohup npm run dev > frontend.log 2>&1 & echo $! > frontend.pid
```

### View Logs
```bash
# Backend
tail -f backend/backend.log

# Frontend
tail -f frontend/frontend.log
```

---

## 📋 What's Built

### Backend (100% Complete) ✅
- Authentication (JWT)
- Transaction CRUD
- Budget Management
- Category Management
- Analytics & Reports
- Database with Flyway

### Frontend (Infrastructure Ready) ⏳
- React + TypeScript + Vite
- Tailwind CSS
- Project structure
- **Next:** Build UI pages

---

## 🎨 Next Steps: Frontend Development

### Install Additional Libraries
```bash
cd frontend

npm install @tanstack/react-query
npm install react-router-dom
npm install react-hook-form zod
npm install recharts
npm install date-fns
npm install lucide-react
```

### Create Pages
1. **Login/Register** - Authentication UI
2. **Dashboard** - Summary cards & charts
3. **Transactions** - List, filter, CRUD
4. **Budgets** - Budget tracking
5. **Analytics** - Charts & insights

---

## 📚 Full Documentation

- **PROJECT_STATUS.md** - Complete status & API docs
- **START_HERE.md** - Previous session handoff
- **Expense_Tracker.pdf** - Full 30-task implementation plan
- **docs/** - Technical documentation

---

## 🐛 Quick Troubleshooting

### Backend not responding?
```bash
# Check logs
tail -50 backend/backend.log

# Restart
kill $(cat backend/backend.pid)
cd backend && JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 \
  nohup mvn spring-boot:run > backend.log 2>&1 & echo $! > backend.pid
```

### Frontend not loading?
```bash
# Check logs
tail -20 frontend/frontend.log

# Restart
kill $(cat frontend/frontend.pid)
cd frontend && nohup npm run dev > frontend.log 2>&1 & echo $! > frontend.pid
```

### Database issues?
```bash
# Restart PostgreSQL
docker compose restart

# Check health
docker exec expense-tracker-db pg_isready -U postgres
```

---

## ✅ Health Check Command

Run this to verify everything:
```bash
echo "Backend:" && curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8080/api/v1/auth/test
echo "Frontend:" && curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:5173
echo "Database:" && docker exec expense-tracker-db pg_isready -U postgres
```

---

**Everything is ready! Start building the frontend! 🎉**
