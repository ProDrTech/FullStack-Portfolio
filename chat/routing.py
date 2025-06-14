# chat/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Oddiy foydalanuvchi uchun
    re_path(r"ws/chat/$", consumers.UserChatConsumer.as_asgi()),

    # Admin uchun
    re_path(r"ws/chat/(?P<user_id>\d+)/$", consumers.AdminChatConsumer.as_asgi()),
]
