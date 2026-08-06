import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { useAuth } from '../contexts/AuthContext';
import { budgets } from '../api';
import type { BudgetProgress } from '../types';
import BudgetForm from '../components/BudgetForm';

const BudgetsPage = () => {
  const { user } = useAuth();
  const queryClient = useQueryClient();
  const [showForm, setShowForm] = useState(false);
  const [editingBudget, setEditingBudget] = useState<BudgetProgress | null>(null);

  // Fetch budgets with progress
  const { data: budgetsData, isLoading } = useQuery({
    queryKey: ['budgets', user?.householdId],
    queryFn: () => budgets.getAll(user!.householdId),
    enabled: !!user,
    refetchInterval: 30000, // Auto-refresh every 30 seconds
  });

  // Delete mutation
  const deleteMutation = useMutation({
    mutationFn: (budgetId: number) => budgets.delete(user!.householdId, budgetId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['budgets'] });
      queryClient.invalidateQueries({ queryKey: ['dashboard'] });
    },
  });

  const handleAdd = () => {
    setEditingBudget(null);
    setShowForm(true);
  };

  const handleEdit = (budgetProgress: BudgetProgress) => {
    setEditingBudget(budgetProgress);
    setShowForm(true);
  };

  const handleClose = () => {
    setShowForm(false);
    setEditingBudget(null);
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'OK':
        return 'bg-green-500';
      case 'WARNING':
        return 'bg-yellow-500';
      case 'EXCEEDED':
        return 'bg-red-500';
      default:
        return 'bg-gray-500';
    }
  };

  const getStatusBadge = (status: string) => {
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

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-gray-500">Loading budgets...</div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Budgets</h1>
        <button
          onClick={handleAdd}
          className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors"
        >
          + Create Budget
        </button>
      </div>

      {/* Budget Grid */}
      {budgetsData && budgetsData.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {budgetsData.map((budgetProgress) => (
            <div
              key={budgetProgress.budget.id}
              className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow"
            >
              <div className="p-6">
                {/* Header */}
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-lg font-bold text-gray-900">
                      {budgetProgress.budget.name}
                    </h3>
                    <p className="text-sm text-gray-500">
                      {budgetProgress.budget.periodType.toLowerCase()}
                    </p>
                  </div>
                  <span
                    className={`px-2 py-1 text-xs rounded-full font-medium ${getStatusBadge(
                      budgetProgress.alertStatus
                    )}`}
                  >
                    {budgetProgress.alertStatus}
                  </span>
                </div>

                {/* Progress Bar */}
                <div className="mb-4">
                  <div className="flex justify-between text-sm mb-2">
                    <span className="text-gray-600">Progress</span>
                    <span className="font-medium text-gray-900">
                      {budgetProgress.percentage.toFixed(1)}%
                    </span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-3">
                    <div
                      className={`h-3 rounded-full transition-all ${getStatusColor(
                        budgetProgress.alertStatus
                      )}`}
                      style={{
                        width: `${Math.min(budgetProgress.percentage, 100)}%`,
                      }}
                    />
                  </div>
                </div>

                {/* Amounts */}
                <div className="space-y-2 mb-4">
                  <div className="flex justify-between text-sm">
                    <span className="text-gray-600">Spent</span>
                    <span className="font-semibold text-gray-900">
                      ${budgetProgress.spent.toFixed(2)}
                    </span>
                  </div>
                  <div className="flex justify-between text-sm">
                    <span className="text-gray-600">Budget</span>
                    <span className="font-semibold text-gray-900">
                      ${budgetProgress.budget.amount.toFixed(2)}
                    </span>
                  </div>
                  <div className="flex justify-between text-sm pt-2 border-t">
                    <span className="text-gray-600">Remaining</span>
                    <span
                      className={`font-bold ${
                        budgetProgress.remaining >= 0
                          ? 'text-green-600'
                          : 'text-red-600'
                      }`}
                    >
                      ${Math.abs(budgetProgress.remaining).toFixed(2)}
                      {budgetProgress.remaining < 0 && ' over'}
                    </span>
                  </div>
                </div>

                {/* Period Info */}
                <div className="text-sm text-gray-500 mb-4">
                  <div className="flex justify-between">
                    <span>Period</span>
                    <span>
                      {new Date(budgetProgress.budget.startDate).toLocaleDateString()} -{' '}
                      {new Date(budgetProgress.budget.endDate).toLocaleDateString()}
                    </span>
                  </div>
                  <div className="flex justify-between mt-1">
                    <span>Days remaining</span>
                    <span className="font-medium">
                      {budgetProgress.daysRemaining} days
                    </span>
                  </div>
                </div>

                {/* Actions */}
                <div className="flex space-x-2 pt-4 border-t">
                  <button
                    onClick={() => handleEdit(budgetProgress)}
                    className="flex-1 text-blue-600 hover:text-blue-800 font-medium text-sm"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => {
                      if (confirm(`Delete budget "${budgetProgress.budget.name}"?`)) {
                        deleteMutation.mutate(budgetProgress.budget.id);
                      }
                    }}
                    className="flex-1 text-red-600 hover:text-red-800 font-medium text-sm"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="bg-white rounded-lg shadow p-12 text-center">
          <div className="text-gray-400 text-6xl mb-4">💰</div>
          <h3 className="text-xl font-medium text-gray-900 mb-2">
            No budgets yet
          </h3>
          <p className="text-gray-500 mb-6">
            Create your first budget to start tracking your spending goals
          </p>
          <button
            onClick={handleAdd}
            className="bg-blue-600 text-white px-6 py-3 rounded-md hover:bg-blue-700 transition-colors"
          >
            Create Your First Budget
          </button>
        </div>
      )}

      {/* Budget Form Modal */}
      {showForm && (
        <BudgetForm
          budgetProgress={editingBudget}
          onClose={handleClose}
          householdId={user!.householdId}
        />
      )}
    </div>
  );
};

export default BudgetsPage;
