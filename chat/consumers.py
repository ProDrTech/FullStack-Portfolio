import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Message
from channels.db import database_sync_to_async 

User = get_user_model()

# 6‑a. Oddiy foydalanuvchi consumer
class UserChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        if user.is_anonymous:
            await self.close()
            return

        self.group_name = f"chat_{user.id}"   # userga xos kanal
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        text = data["message"]

        admin = await self.get_admin()
        msg = await self.create_msg(sender=self.scope["user"], recipient=admin, text=text)

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat.message",
                "message": text,
                "sender": "user"
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def get_admin(self):
        return User.objects.filter(is_superuser=True).first()

    @database_sync_to_async
    def create_msg(self, **kwargs):
        return Message.objects.create(**kwargs)

# 6‑b. Admin panel consumer
class AdminChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if not self.scope["user"].is_staff:
            await self.close()
            return

        self.target_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.group_name = f"chat_{self.target_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        text = data["message"]

        target = await self.get_user(self.target_id)
        sender = self.scope["user"]

        await self.create_msg(sender=sender, recipient=target, text=text)

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat.message",
                "message": text,
                "sender": "admin"
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def get_user(self, pk):
        return User.objects.get(pk=pk)

    @database_sync_to_async
    def create_msg(self, **kwargs):
        return Message.objects.create(**kwargs)
