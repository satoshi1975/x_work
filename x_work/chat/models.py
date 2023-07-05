'''chat models'''
from django.db import models
from main.models import User
from employers.models import Employer
from job_seekers.models import JobSeeker


class ChatRoom(models.Model):
    '''model of chat room'''
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name='chatrooms_user1')
    jobseeker = models.ForeignKey(
        JobSeeker,
        on_delete=models.CASCADE,
        related_name='chatrooms_user2')
    chat_id = models.CharField(max_length=100, unique=True)


class BlockList(models.Model):
    '''model of block list'''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user')
    blocked_user = models.ManyToManyField(User, related_name='blocked_user')
