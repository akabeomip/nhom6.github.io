"""
ASGI config for newdjangoproject4 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import nguoidung.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newdjangoproject4.settings')

application = get_asgi_application({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
    URLRouter(
      nguoidung.routing.websocket_urlpatterns
    )
  )
})