from django.urls import path
from .consumers import TaskConsumer, TaskLogConsumer

task_urlpatterns = [
    path('ws/tasks/', TaskConsumer.as_asgi()),
    path('ws/tasklogs/', TaskLogConsumer.as_asgi()),
]