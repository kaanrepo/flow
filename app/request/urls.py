from django.urls import path
from .views import RequestListCreateView, RequestRetrieveUpdateDestroyView, EmployeeRequestListView


urlpatterns = [
    path('', RequestListCreateView.as_view(), name='request-list-create-view'),
    path('<int:pk>/', RequestRetrieveUpdateDestroyView.as_view(), name='request-retrieve-update-destroy-view'),
    path('employee/<int:pk>/', EmployeeRequestListView.as_view(), name='employee-request-list-view'),
]
