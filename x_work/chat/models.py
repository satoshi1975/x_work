from django.db import models
from main.models import User

class ChatRoom(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatrooms_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatrooms_user2')
    chat_id = models.CharField(max_length=100, unique=True)