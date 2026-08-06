# Expense Tracker - Continue Implementation Guide

## Current Status: 9/14 Tasks Complete (64%)
## Time: 3:20 PM, Day 1 | Remaining: ~6 hours today, 12 hours tomorrow

---

## ✅ What's Working Right Now

### Backend (100% Complete)
- **Server:** Running on http://localhost:8080
- **Database:** PostgreSQL with 5 tables + seed data
- **Auth:** JWT tokens working
- **All 20 API endpoints functional**

### Frontend (64% Complete)
- **Server:** Running on http://localhost:5173
- **Login/Register:** Full authentication flow
- **Navigation:** Layout with routing
- **API Client:** Axios with JWT interceptor

---

## 🎯 Test It Now!

1. Open http://localhost:5173
2. Click "Register here"
3. Create account (email: test@test.com, password: Test1234!, name: Test User)
4. You'll be auto-logged in and see the Dashboard placeholder
5. Try navigating between pages using the top menu

---

## 📋 Remaining Tasks (5 tasks, ~14-16 hours)

### Task 10: Transaction Management UI (3-4 hours) - NEXT
### Task 11: Budget Management UI (2-3 hours)
### Task 12: Dashboard with Charts (2-3 hours)
### Task 13: Trend Analytics Page (1.5-2 hours)
### Task 14: Category Management + Polish (1.5-2 hours)

---

## 🚀 TASK 10: Transaction Management UI (Start Here)

### What to Build:
Full-featured transaction table with:
- List all transactions with pagination
- Filter by date range, category, type, payment method
- Search by description
- Add/Edit/Delete transactions
- Bulk delete selected transactions

### Step 1: Install date picker (Optional, but recommended)
```bash
cd frontend
npm install react-datepicker @types/react-datepicker
```

### Step 2: Create TransactionsPage (Replace placeholder)

```tsx
// src/pages/TransactionsPage.tsx
import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { useAuth } from '../contexts/AuthContext';
import { transactions } from '../api';
import type { Transaction, TransactionRequest } from '../types';

const TransactionsPage = () => {
  const { user } = useAuth();
  const queryClient = useQueryClient();
  
  // State
  const [page, setPage] = useState(0);
  const [search, setSearch] = useState('');
  const [selectedIds, setSelectedIds] = useState<number[]>([]);
  const [showForm, setShowForm] = useState(false);
  const [editingTransaction, setEditingTransaction] = useState<Transaction | null>(null);

  // Fetch transactions
  const { data, isLoading } = useQuery({
    queryKey: ['transactions', user?.householdId, page, search],
    queryFn: () => transactions.getAll(user!.householdId, { page, size: 10, search }),
    enabled: !!user,
  });

  // Delete mutation
  const deleteMutation = useMutation({
    mutationFn: (id: number) => transactions.delete(user!.householdId, id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['transactions'] }),
  });

  // Bulk delete mutation
  const bulkDeleteMutation = useMutation({
    mutationFn: () => transactions.bulkDelete(user!.householdId, selectedIds),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['transactions'] });
      setSelectedIds([]);
    },
  });

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Transactions</h1>
        <button
          onClick={() => {
            setEditingTransaction(null);
            setShowForm(true);
          }}
          className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          + Add Transaction
        </button>
      </div>

      {/* Search & Filters */}
      <div className="bg-white p-4 rounded-lg shadow mb-4">
        <input
          type="text"
          placeholder="Search transactions..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full px-3 py-2 border rounded-md"
        />
      </div>

      {/* Bulk Actions */}
      {selectedIds.length > 0 && (
        <div className="bg-blue-50 p-3 rounded-lg mb-4 flex justify-between items-center">
          <span>{selectedIds.length} selected</span>
          <button
            onClick={() => bulkDeleteMutation.mutate()}
            className="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700"
          >
            Delete Selected
          </button>
        </div>
      )}

      {/* Transaction Table */}
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="min-w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                <input
                  type="checkbox"
                  checked={selectedIds.length === data?.content.length}
                  onChange={(e) => {
                    if (e.target.checked) {
                      setSelectedIds(data!.content.map(t => t.id));
                    } else {
                      setSelectedIds([]);
                    }
                  }}
                />
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Date</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Amount</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Type</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {data?.content.map((transaction) => (
              <tr key={transaction.id}>
                <td className="px-6 py-4">
                  <input
                    type="checkbox"
                    checked={selectedIds.includes(transaction.id)}
                    onChange={(e) => {
                      if (e.target.checked) {
                        setSelectedIds([...selectedIds, transaction.id]);
                      } else {
                        setSelectedIds(selectedIds.filter(id => id !== transaction.id));
                      }
                    }}
                  />
                </td>
                <td className="px-6 py-4 text-sm text-gray-900">
                  {new Date(transaction.transactionDate).toLocaleDateString()}
                </td>
                <td className="px-6 py-4 text-sm text-gray-900">{transaction.description}</td>
                <td className="px-6 py-4 text-sm text-gray-900">
                  ${transaction.amount.toFixed(2)}
                </td>
                <td className="px-6 py-4 text-sm">
                  <span
                    className={`px-2 py-1 text-xs rounded-full ${
                      transaction.type === 'EXPENSE'
                        ? 'bg-red-100 text-red-800'
                        : 'bg-green-100 text-green-800'
                    }`}
                  >
                    {transaction.type}
                  </span>
                </td>
                <td className="px-6 py-4 text-sm space-x-2">
                  <button
                    onClick={() => {
                      setEditingTransaction(transaction);
                      setShowForm(true);
                    }}
                    className="text-blue-600 hover:text-blue-800"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => deleteMutation.mutate(transaction.id)}
                    className="text-red-600 hover:text-red-800"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Pagination */}
      <div className="mt-4 flex justify-between items-center">
        <button
          onClick={() => setPage(p => Math.max(0, p - 1))}
          disabled={page === 0}
          className="px-4 py-2 border rounded-md disabled:opacity-50"
        >
          Previous
        </button>
        <span>Page {page + 1} of {data?.totalPages || 1}</span>
        <button
          onClick={() => setPage(p => p + 1)}
          disabled={page >= (data?.totalPages || 1) - 1}
          className="px-4 py-2 border rounded-md disabled:opacity-50"
        >
          Next
        </button>
      </div>

      {/* Transaction Form Modal (simplified - add full form later) */}
      {showForm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div className="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
            <h3 className="text-lg font-bold mb-4">
              {editingTransaction ? 'Edit Transaction' : 'Add Transaction'}
            </h3>
            {/* Add your form fields here */}
            <button
              onClick={() => setShowForm(false)}
              className="mt-4 w-full bg-gray-200 px-4 py-2 rounded-md hover:bg-gray-300"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default TransactionsPage;
```

### Step 3: Add Transaction Form Component

Create `src/components/TransactionForm.tsx` with form fields for:
- Amount (number input)
- Type (select: EXPENSE/INCOME)
- Category (select from categories API)
- Description (textarea)
- Date (date picker)
- Payment Method (input)

Use React Hook Form + Zod for validation.

### Step 4: Test
1. Refresh http://localhost:5173/transactions
2. Click "Add Transaction"
3. Fill form and submit
4. See transaction in table
5. Try edit, delete, bulk delete

---

## 📊 Quick Reference: All Remaining Components

### Task 11: Budgets (BudgetsPage.tsx)
- Grid of budget cards
- Progress bar showing spent/total
- Color-coded by alert status (green/yellow/red)
- Add/Edit/Delete dialogs

### Task 12: Dashboard (DashboardPage.tsx)
- 3 summary cards (expense/income/balance)
- Pie chart using Recharts
- Recent transactions list
- Active budgets preview

### Task 13: Analytics (AnalyticsPage.tsx)
- Line chart for monthly trends
- Bar chart for category breakdown
- Period selector (3/6/12 months)

### Task 14: Polish
- Category management page
- Loading skeletons
- Toast notifications for errors
- Mobile responsive tweaks

---

## 💡 Pro Tips

1. **Use TanStack Query patterns:**
```tsx
const { data } = useQuery({
  queryKey: ['key', param],
  queryFn: () => api.function(param),
});

const mutation = useMutation({
  mutationFn: api.function,
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ['key'] }),
});
```

2. **Recharts Example:**
```tsx
import { PieChart, Pie, Cell } from 'recharts';

<PieChart width={400} height={400}>
  <Pie data={data} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={80}>
    {data.map((entry, index) => (
      <Cell key={index} fill={COLORS[index % COLORS.length]} />
    ))}
  </Pie>
</PieChart>
```

3. **Date Formatting:**
```tsx
import { format } from 'date-fns';
format(new Date(dateString), 'MMM d, yyyy')
```

---

## 🎯 Priority Order

1. **Tonight (4-6 hours):** Complete Task 10 (Transactions)
2. **Tomorrow Morning (3-4 hours):** Tasks 11-12 (Budgets + Dashboard)
3. **Tomorrow Afternoon (3-4 hours):** Tasks 13-14 (Analytics + Polish)
4. **Tomorrow Evening:** Final testing and demo prep

---

## 🔧 Useful Commands

```bash
# Stop/Start servers
cd /home/govind/Desktop/project/backend
kill $(cat backend.pid) && JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 nohup mvn spring-boot:run > backend.log 2>&1 &

cd /home/govind/Desktop/project/frontend
kill $(cat frontend.pid) && nohup npm run dev > frontend.log 2>&1 &

# View logs
tail -f backend/backend.log
tail -f frontend/frontend.log

# Test API directly
curl http://localhost:8080/api/v1/households/1/categories -H "Authorization: Bearer YOUR_TOKEN"
```

---

## ✅ Success Criteria

By end of Day 2, you should have:
- ✓ Working registration and login
- ✓ Can add/edit/delete transactions with filters
- ✓ Can create budgets and see progress with alerts
- ✓ Dashboard showing summary and charts
- ✓ Analytics showing trends
- ✓ Responsive design on mobile/tablet/desktop

---

## 🚀 You're 64% Done!

Backend is 100% complete. Frontend auth is working. Just 5 more UI tasks to go!

**Next Action:** Open http://localhost:5173, verify login works, then start building the transactions table above.

Good luck! 🎉
