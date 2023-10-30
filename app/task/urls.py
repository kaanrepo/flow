from django.urls import path

from .views import TaskListCreateView,EmployeeTaskListView, TaskDetailView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='tasks-list-create-view'),
    path('employee/<uuid:uuid>/', EmployeeTaskListView.as_view(), name='employee-tasks-view'),
    path('<uuid:uuid>/', TaskDetailView.as_view(), name='task-detail-view')
]
