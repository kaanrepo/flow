from django.urls import path

from .views import TaskListCreateView,EmployeeTaskListView, TaskDetailView, TaskDashboardView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='tasks-list-create-view'),
    path('dashboard/', TaskDashboardView.as_view(), name='tasks-dashboard-view'),
    path('employee/<int:pk>/', EmployeeTaskListView.as_view(), name='employee-tasks-view'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail-view')
]
