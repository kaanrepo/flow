"""
ASGI config for flow project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from task.routing import task_urlpatterns
from request.routing import request_urlpatterns

websocket_urlpatterns = task_urlpatterns + request_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow.settings')

django_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_application,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(
            websocket_urlpatterns)
        )
    ),
})
