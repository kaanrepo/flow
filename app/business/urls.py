from django.urls import path
from .views import (EmployeeListCreateView, EmployeeDetailView, TeamListCreateView,
                    TeamDetailView, CustomerListCreateView, CustomerDetailView, CurrentEmployeeView)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('current-employee/', CurrentEmployeeView.as_view(), name='current-employee'),
]