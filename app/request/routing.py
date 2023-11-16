from django.urls import path

from .consumers import RequestConsumer

request_urlpatterns = [
    path('ws/requests/', RequestConsumer.as_asgi()),
]