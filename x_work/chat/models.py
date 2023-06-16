from django.db import models
from main.models import User
from employers.models import Employer
from job_seekers.models import JobSeeker
class ChatRoom(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='chatrooms_user1')
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='chatrooms_user2')
    chat_id = models.CharField(max_length=100, unique=True)