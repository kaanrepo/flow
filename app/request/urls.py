from django.urls import path
from .views import RequestListCreateView, RequestRetrieveUpdateDestroyView, EmployeeRequestListView


urlpatterns = [
    path('', RequestListCreateView.as_view(), name='request-list-create-view'),
    path('<uuid:uuid>/', RequestRetrieveUpdateDestroyView.as_view(), name='request-retrieve-update-destroy-view'),
    path('employee/<uuid:uuid>/', EmployeeRequestListView.as_view(), name='employee-request-list-view'),
]
