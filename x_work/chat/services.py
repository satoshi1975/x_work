from main.models import User
from employers.models import Employer
from job_seekers.models import JobSeeker
from chat.models import ChatRoom
from django.db.models import Q
from uuid import uuid4

class ChatManager:
    
    @staticmethod
    def create_chat(employer, jobseeker):
        chat_id=ChatRoom.objects.create(employer=employer,jobseeker=jobseeker,chat_id=uuid4().int).chat_id
        # chat_id=uuid4().int
        # chat=ChatRoom.objects.create(user1=user1,user2=user2,chat_id=chat_id)
        return chat_id



    @staticmethod
    def get_chat_id(jobseeker_id,employer_id):
        # user2=User.objects.get(id=user2_id)
        jobseeker=JobSeeker.objects.get(user_id=jobseeker_id)
        employer=Employer.objects.get(user_id=employer_id)
        try:
            chat_id=ChatRoom.objects.get(employer=employer,jobseeker=jobseeker).chat_id
        except:
            chat_id=ChatManager().create_chat(employer=employer,jobseeker=jobseeker)
        return chat_id

    @staticmethod
    def get_recipient_context(user_id):
        user = User.objects.get(id=user_id)
        if user.user_type == 'jobseeker':
            return JobSeeker.objects.get(user=user)
        else:
            return Employer.objects.get(user=user)

    @staticmethod
    def get_sender_context(user_id):
        return User.objects.get(id=user_id)
    
    @staticmethod
    def get_chat_list(user_id):
        user=User.objects.get(id=user_id)
        if user.user_type=='company':
            return ChatRoom.objects.filter(employer=Employer.objects.get(user=user))
        else:
            return ChatRoom.objects.filter(jobseeker=JobSeeker.objects.get(user=user))
        # chat_list=ChatRoom.objects.filter(Q(jobseeker=user)|Q(employer=user))
        # return chat_list