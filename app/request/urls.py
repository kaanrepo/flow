from django.urls import path
from .views import RequestListCreateView, RequestRetrieveUpdateDestroyView, EmployeeRequestListView, TeamPendingRequestListView


urlpatterns = [
    path('', RequestListCreateView.as_view(), name='request-list-create-view'),
    path('<int:pk>/', RequestRetrieveUpdateDestroyView.as_view(), name='request-retrieve-update-destroy-view'),
    path('employee/<int:pk>/', EmployeeRequestListView.as_view(), name='employee-request-list-view'),
    path('team/<int:pk>/', TeamPendingRequestListView.as_view(), name='team-pending-request-list-view')
]
