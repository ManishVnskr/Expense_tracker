export interface User {
  id: number;
  email: string;
  fullName: string;
  householdId: number;
  createdAt: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  password: string;
  fullName: string;
}

export interface LoginResponse {
  token: string;
  type: string;
  expiresIn: number;
  user: User;
}

export interface Category {
  id: number;
  householdId: number;
  name: string;
  type: 'EXPENSE' | 'INCOME';
  icon?: string;
  color?: string;
  isDefault: boolean;
  createdAt: string;
}

export interface Transaction {
  id: number;
  householdId: number;
  categoryId?: number;
  amount: number;
  type: 'EXPENSE' | 'INCOME';
  description?: string;
  transactionDate: string;
  paymentMethod?: string;
  tags?: string[];
  createdAt: string;
  updatedAt: string;
}

export interface TransactionRequest {
  amount: number;
  type: 'EXPENSE' | 'INCOME';
  categoryId?: number;
  description?: string;
  transactionDate: string;
  paymentMethod?: string;
  tags?: string[];
}

export interface Budget {
  id: number;
  householdId: number;
  name: string;
  amount: number;
  periodType: 'WEEKLY' | 'MONTHLY' | 'YEARLY';
  startDate: string;
  endDate: string;
  alertThreshold: number;
  createdAt: string;
  updatedAt: string;
}

export interface BudgetRequest {
  name: string;
  amount: number;
  periodType: 'WEEKLY' | 'MONTHLY' | 'YEARLY';
  startDate: string;
  endDate: string;
  alertThreshold?: number;
}

export interface BudgetProgress {
  budget: Budget;
  spent: number;
  remaining: number;
  percentage: number;
  alertStatus: 'OK' | 'WARNING' | 'EXCEEDED';
  daysRemaining: number;
}

export interface DashboardData {
  totalExpense: number;
  totalIncome: number;
  balance: number;
  expensesByCategory: CategorySummary[];
  recentTransactions: TransactionSummary[];
  activeBudgets: BudgetProgress[];
}

export interface CategorySummary {
  categoryId: number;
  categoryName: string;
  amount: number;
  percentage: number;
}

export interface TransactionSummary {
  id: number;
  amount: number;
  type: string;
  description?: string;
  transactionDate: string;
  categoryName: string;
}

export interface TrendsData {
  monthlyExpenses: MonthlyData[];
  monthlyIncome: MonthlyData[];
  categoryBreakdown: Record<string, number>;
}

export interface MonthlyData {
  month: string;
  amount: number;
  transactionCount: number;
}

export interface PageResponse<T> {
  content: T[];
  totalElements: number;
  totalPages: number;
  size: number;
  number: number;
}
