import { useQuery } from '@tanstack/react-query';
import { useAuth } from '../contexts/AuthContext';
import { analytics } from '../api';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';
import { Link } from 'react-router-dom';

const COLORS = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2'];

const DashboardPage = () => {
  const { user } = useAuth();

  // Fetch dashboard data
  const { data, isLoading } = useQuery({
    queryKey: ['dashboard', user?.householdId],
    queryFn: () => analytics.getDashboard(user!.householdId),
    enabled: !!user,
    refetchInterval: 60000, // Refresh every minute
  });

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-gray-500">Loading dashboard...</div>
      </div>
    );
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'OK':
        return 'bg-green-100 text-green-800';
      case 'WARNING':
        return 'bg-yellow-100 text-yellow-800';
      case 'EXCEEDED':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const pieData = data?.expensesByCategory.map(cat => ({
    name: cat.categoryName,
    value: Number(cat.amount),
    percentage: cat.percentage,
  })) || [];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600 mt-1">Overview of your finances this month</p>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Total Expense */}
        <div className="bg-gradient-to-br from-red-50 to-red-100 rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-red-600 uppercase">Total Expenses</p>
              <p className="text-3xl font-bold text-red-900 mt-2">
                ${data?.totalExpense.toFixed(2) || '0.00'}
              </p>
            </div>
            <div className="text-4xl">📉</div>
          </div>
        </div>

        {/* Total Income */}
        <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-green-600 uppercase">Total Income</p>
              <p className="text-3xl font-bold text-green-900 mt-2">
                ${data?.totalIncome.toFixed(2) || '0.00'}
              </p>
            </div>
            <div className="text-4xl">📈</div>
          </div>
        </div>

        {/* Balance */}
        <div className={`bg-gradient-to-br rounded-lg shadow p-6 ${
          (data?.balance || 0) >= 0 
            ? 'from-blue-50 to-blue-100' 
            : 'from-orange-50 to-orange-100'
        }`}>
          <div className="flex items-center justify-between">
            <div>
              <p className={`text-sm font-medium uppercase ${
                (data?.balance || 0) >= 0 ? 'text-blue-600' : 'text-orange-600'
              }`}>
                Balance
              </p>
              <p className={`text-3xl font-bold mt-2 ${
                (data?.balance || 0) >= 0 ? 'text-blue-900' : 'text-orange-900'
              }`}>
                ${Math.abs(data?.balance || 0).toFixed(2)}
                {(data?.balance || 0) < 0 && ' deficit'}
              </p>
            </div>
            <div className="text-4xl">💰</div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Expenses by Category - Pie Chart */}
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-lg font-bold text-gray-900 mb-4">Expenses by Category</h2>
          {pieData.length > 0 ? (
            <div className="h-80">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={pieData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ percentage }) => `${percentage.toFixed(1)}%`}
                    outerRadius={100}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {pieData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip
                    formatter={(value: number) => `$${value.toFixed(2)}`}
                  />
                  <Legend />
                </PieChart>
              </ResponsiveContainer>
            </div>
          ) : (
            <div className="text-center py-12 text-gray-500">
              <p className="mb-2">No expenses yet this month</p>
              <Link to="/transactions" className="text-blue-600 hover:text-blue-800">
                Add your first transaction
              </Link>
            </div>
          )}
        </div>

        {/* Active Budgets */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-lg font-bold text-gray-900">Active Budgets</h2>
            <Link to="/budgets" className="text-sm text-blue-600 hover:text-blue-800">
              View all
            </Link>
          </div>
          {data?.activeBudgets && data.activeBudgets.length > 0 ? (
            <div className="space-y-4">
              {data.activeBudgets.slice(0, 5).map((budgetProgress) => (
                <div key={budgetProgress.budget.id} className="border-b last:border-b-0 pb-4 last:pb-0">
                  <div className="flex justify-between items-start mb-2">
                    <div>
                      <h3 className="font-medium text-gray-900">{budgetProgress.budget.name}</h3>
                      <p className="text-xs text-gray-500">
                        {budgetProgress.daysRemaining} days remaining
                      </p>
                    </div>
                    <span className={`px-2 py-1 text-xs rounded-full ${getStatusColor(budgetProgress.alertStatus)}`}>
                      {budgetProgress.alertStatus}
                    </span>
                  </div>
                  <div className="mb-1">
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className={`h-2 rounded-full transition-all ${
                          budgetProgress.alertStatus === 'OK'
                            ? 'bg-green-500'
                            : budgetProgress.alertStatus === 'WARNING'
                            ? 'bg-yellow-500'
                            : 'bg-red-500'
                        }`}
                        style={{ width: `${Math.min(budgetProgress.percentage, 100)}%` }}
                      />
                    </div>
                  </div>
                  <div className="flex justify-between text-xs text-gray-600">
                    <span>${budgetProgress.spent.toFixed(2)} spent</span>
                    <span>${budgetProgress.budget.amount.toFixed(2)} budget</span>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-12 text-gray-500">
              <p className="mb-2">No active budgets</p>
              <Link to="/budgets" className="text-blue-600 hover:text-blue-800">
                Create your first budget
              </Link>
            </div>
          )}
        </div>
      </div>

      {/* Recent Transactions */}
      <div className="bg-white rounded-lg shadow">
        <div className="p-6 border-b border-gray-200">
          <div className="flex justify-between items-center">
            <h2 className="text-lg font-bold text-gray-900">Recent Transactions</h2>
            <Link to="/transactions" className="text-sm text-blue-600 hover:text-blue-800">
              View all
            </Link>
          </div>
        </div>
        {data?.recentTransactions && data.recentTransactions.length > 0 ? (
          <div className="divide-y divide-gray-200">
            {data.recentTransactions.map((transaction) => (
              <div key={transaction.id} className="p-4 hover:bg-gray-50 transition-colors">
                <div className="flex justify-between items-center">
                  <div className="flex-1">
                    <div className="flex items-center space-x-3">
                      <span
                        className={`px-2 py-1 text-xs rounded-full ${
                          transaction.type === 'EXPENSE'
                            ? 'bg-red-100 text-red-800'
                            : 'bg-green-100 text-green-800'
                        }`}
                      >
                        {transaction.type}
                      </span>
                      <span className="font-medium text-gray-900">
                        {transaction.description || 'No description'}
                      </span>
                    </div>
                    <div className="flex items-center space-x-4 mt-1">
                      <span className="text-sm text-gray-500">{transaction.categoryName}</span>
                      <span className="text-sm text-gray-400">
                        {new Date(transaction.transactionDate).toLocaleDateString('en-US', {
                          month: 'short',
                          day: 'numeric',
                        })}
                      </span>
                    </div>
                  </div>
                  <div className={`text-lg font-bold ${
                    transaction.type === 'EXPENSE' ? 'text-red-600' : 'text-green-600'
                  }`}>
                    {transaction.type === 'EXPENSE' ? '-' : '+'}${transaction.amount.toFixed(2)}
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-12 text-gray-500">
            <p className="mb-2">No recent transactions</p>
            <Link to="/transactions" className="text-blue-600 hover:text-blue-800">
              Add your first transaction
            </Link>
          </div>
        )}
      </div>
    </div>
  );
};

export default DashboardPage;
