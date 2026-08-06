import apiClient from './client';
import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  User,
  Category,
  Transaction,
  TransactionRequest,
  Budget,
  BudgetRequest,
  BudgetProgress,
  DashboardData,
  TrendsData,
  PageResponse,
} from '../types';

// Auth APIs
export const auth = {
  login: async (data: LoginRequest): Promise<LoginResponse> => {
    const response = await apiClient.post<LoginResponse>('/auth/login', data);
    return response.data;
  },

  register: async (data: RegisterRequest): Promise<User> => {
    const response = await apiClient.post<User>('/auth/register', data);
    return response.data;
  },

  getCurrentUser: async (): Promise<User> => {
    const response = await apiClient.get<User>('/users/me');
    return response.data;
  },
};

// Category APIs
export const categories = {
  getAll: async (householdId: number): Promise<Category[]> => {
    const response = await apiClient.get<Category[]>(`/households/${householdId}/categories`);
    return response.data;
  },

  create: async (householdId: number, data: Partial<Category>): Promise<Category> => {
    const response = await apiClient.post<Category>(`/households/${householdId}/categories`, data);
    return response.data;
  },

  delete: async (householdId: number, categoryId: number): Promise<void> => {
    await apiClient.delete(`/households/${householdId}/categories/${categoryId}`);
  },
};

// Transaction APIs
export const transactions = {
  getAll: async (
    householdId: number,
    params?: {
      startDate?: string;
      endDate?: string;
      categoryId?: number;
      type?: 'EXPENSE' | 'INCOME';
      paymentMethod?: string;
      search?: string;
      page?: number;
      size?: number;
    }
  ): Promise<PageResponse<Transaction>> => {
    const response = await apiClient.get<PageResponse<Transaction>>(
      `/households/${householdId}/transactions`,
      { params }
    );
    return response.data;
  },

  create: async (householdId: number, data: TransactionRequest): Promise<Transaction> => {
    const response = await apiClient.post<Transaction>(
      `/households/${householdId}/transactions`,
      data
    );
    return response.data;
  },

  update: async (
    householdId: number,
    transactionId: number,
    data: TransactionRequest
  ): Promise<Transaction> => {
    const response = await apiClient.put<Transaction>(
      `/households/${householdId}/transactions/${transactionId}`,
      data
    );
    return response.data;
  },

  delete: async (householdId: number, transactionId: number): Promise<void> => {
    await apiClient.delete(`/households/${householdId}/transactions/${transactionId}`);
  },

  bulkDelete: async (householdId: number, transactionIds: number[]): Promise<void> => {
    await apiClient.delete(`/households/${householdId}/transactions/bulk`, {
      data: transactionIds,
    });
  },
};

// Budget APIs
export const budgets = {
  getAll: async (householdId: number): Promise<BudgetProgress[]> => {
    const response = await apiClient.get<BudgetProgress[]>(`/households/${householdId}/budgets`);
    return response.data;
  },

  get: async (householdId: number, budgetId: number): Promise<BudgetProgress> => {
    const response = await apiClient.get<BudgetProgress>(
      `/households/${householdId}/budgets/${budgetId}`
    );
    return response.data;
  },

  create: async (householdId: number, data: BudgetRequest): Promise<Budget> => {
    const response = await apiClient.post<Budget>(`/households/${householdId}/budgets`, data);
    return response.data;
  },

  update: async (householdId: number, budgetId: number, data: BudgetRequest): Promise<Budget> => {
    const response = await apiClient.put<Budget>(
      `/households/${householdId}/budgets/${budgetId}`,
      data
    );
    return response.data;
  },

  delete: async (householdId: number, budgetId: number): Promise<void> => {
    await apiClient.delete(`/households/${householdId}/budgets/${budgetId}`);
  },
};

// Analytics APIs
export const analytics = {
  getDashboard: async (householdId: number): Promise<DashboardData> => {
    const response = await apiClient.get<DashboardData>(
      `/households/${householdId}/analytics/dashboard`
    );
    return response.data;
  },

  getTrends: async (householdId: number, months: number = 6): Promise<TrendsData> => {
    const response = await apiClient.get<TrendsData>(
      `/households/${householdId}/analytics/trends`,
      { params: { months } }
    );
    return response.data;
  },
};
