import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { useAuth } from '../contexts/AuthContext';
import { analytics } from '../api';
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';

const AnalyticsPage = () => {
  const { user } = useAuth();
  const [months, setMonths] = useState(6);

  // Fetch trends data
  const { data, isLoading } = useQuery({
    queryKey: ['trends', user?.householdId, months],
    queryFn: () => analytics.getTrends(user!.householdId, months),
    enabled: !!user,
  });

  const lineChartData = data?.monthlyExpenses.map((expense, index) => ({
    month: expense.month,
    expenses: Number(expense.amount),
    income: Number(data.monthlyIncome[index]?.amount || 0),
  })) || [];

  const categoryData = Object.entries(data?.categoryBreakdown || {})
    .map(([name, amount]) => ({
      name,
      amount: Number(amount),
    }))
    .sort((a, b) => b.amount - a.amount)
    .slice(0, 10); // Top 10 categories

  const totalExpenses = lineChartData.reduce((sum, item) => sum + item.expenses, 0);
  const totalIncome = lineChartData.reduce((sum, item) => sum + item.income, 0);
  const avgExpenses = totalExpenses / (lineChartData.length || 1);
  const avgIncome = totalIncome / (lineChartData.length || 1);

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-gray-500">Loading analytics...</div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Analytics</h1>
          <p className="text-gray-600 mt-1">Track your spending trends over time</p>
        </div>
        {/* Period Selector */}
        <div className="flex space-x-2">
          <button
            onClick={() => setMonths(3)}
            className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
              months === 3
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            3 Months
          </button>
          <button
            onClick={() => setMonths(6)}
            className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
              months === 6
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            6 Months
          </button>
          <button
            onClick={() => setMonths(12)}
            className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
              months === 12
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            12 Months
          </button>
        </div>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-lg shadow p-4">
          <p className="text-sm text-gray-600">Total Expenses</p>
          <p className="text-2xl font-bold text-red-600 mt-1">
            ${totalExpenses.toFixed(2)}
          </p>
        </div>
        <div className="bg-white rounded-lg shadow p-4">
          <p className="text-sm text-gray-600">Total Income</p>
          <p className="text-2xl font-bold text-green-600 mt-1">
            ${totalIncome.toFixed(2)}
          </p>
        </div>
        <div className="bg-white rounded-lg shadow p-4">
          <p className="text-sm text-gray-600">Avg. Monthly Expenses</p>
          <p className="text-2xl font-bold text-gray-900 mt-1">
            ${avgExpenses.toFixed(2)}
          </p>
        </div>
        <div className="bg-white rounded-lg shadow p-4">
          <p className="text-sm text-gray-600">Avg. Monthly Income</p>
          <p className="text-2xl font-bold text-gray-900 mt-1">
            ${avgIncome.toFixed(2)}
          </p>
        </div>
      </div>

      {/* Monthly Trends - Line Chart */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-lg font-bold text-gray-900 mb-4">
          Income vs Expenses Trend
        </h2>
        {lineChartData.length > 0 ? (
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={lineChartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="month"
                  tick={{ fontSize: 12 }}
                />
                <YAxis
                  tick={{ fontSize: 12 }}
                  tickFormatter={(value) => `$${value}`}
                />
                <Tooltip
                  formatter={(value) => `$${Number(value).toFixed(2)}`}
                />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="expenses"
                  stroke="#ef4444"
                  strokeWidth={2}
                  name="Expenses"
                  dot={{ r: 4 }}
                  activeDot={{ r: 6 }}
                />
                <Line
                  type="monotone"
                  dataKey="income"
                  stroke="#22c55e"
                  strokeWidth={2}
                  name="Income"
                  dot={{ r: 4 }}
                  activeDot={{ r: 6 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        ) : (
          <div className="text-center py-12 text-gray-500">
            No data available for the selected period
          </div>
        )}
      </div>

      {/* Category Breakdown - Bar Chart */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-lg font-bold text-gray-900 mb-4">
          Top Spending Categories
        </h2>
        {categoryData.length > 0 ? (
          <div className="h-96">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart
                data={categoryData}
                layout="vertical"
                margin={{ left: 100 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  type="number"
                  tick={{ fontSize: 12 }}
                  tickFormatter={(value) => `$${value}`}
                />
                <YAxis
                  type="category"
                  dataKey="name"
                  tick={{ fontSize: 12 }}
                  width={90}
                />
                <Tooltip
                  formatter={(value) => `$${Number(value).toFixed(2)}`}
                />
                <Bar
                  dataKey="amount"
                  fill="#3b82f6"
                  radius={[0, 4, 4, 0]}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>
        ) : (
          <div className="text-center py-12 text-gray-500">
            No category data available
          </div>
        )}
      </div>

      {/* Insights */}
      {lineChartData.length > 1 && (
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
          <h3 className="text-lg font-bold text-blue-900 mb-3">💡 Insights</h3>
          <div className="space-y-2 text-sm text-blue-800">
            {totalExpenses > totalIncome && (
              <p>
                ⚠️ Your expenses exceed your income by ${(totalExpenses - totalIncome).toFixed(2)} 
                over the last {months} months.
              </p>
            )}
            {totalIncome > totalExpenses && (
              <p>
                ✅ Great job! You're saving ${(totalIncome - totalExpenses).toFixed(2)} 
                over the last {months} months.
              </p>
            )}
            {categoryData.length > 0 && (
              <p>
                📊 Your top spending category is <strong>{categoryData[0].name}</strong> with 
                ${categoryData[0].amount.toFixed(2)} spent.
              </p>
            )}
            {lineChartData.length > 0 && (
              <p>
                📅 Average monthly expenses: ${avgExpenses.toFixed(2)} | 
                Average monthly income: ${avgIncome.toFixed(2)}
              </p>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default AnalyticsPage;
