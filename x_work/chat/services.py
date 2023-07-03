from main.models import User
from employers.models import Employer
from job_seekers.models import JobSeeker
from chat.models import ChatRoom, BlockList
from django.db.models import Q
from uuid import uuid4

class ChatManager:
    '''a class for chat management'''
    @staticmethod
    def create_chat(employer, jobseeker):
        '''create new chat'''
        if ChatRoom.objects.filter(jobseeker=jobseeker,employer=employer).exists():
            return ChatRoom.objects.get(jobseeker=jobseeker,employer=employer).chat_id
        else:
            chat_id=ChatRoom.objects.create(employer=employer,jobseeker=jobseeker,chat_id=uuid4().int).chat_id
        
        return chat_id

    @staticmethod
    def get_chat_id(jobseeker_id,employer_id):
        '''get chat by job seekers id and employers id'''
        if User.objects.get(id=jobseeker_id).user_type == User.objects.get(id=employer_id).user_type:
            return False
        jobseeker=JobSeeker.objects.get(user_id=jobseeker_id)
        employer=Employer.objects.get(user_id=employer_id)
        try:
            chat_id=ChatRoom.objects.get(employer=employer,jobseeker=jobseeker).chat_id
        except:
            chat_id=ChatManager().create_chat(employer=employer,jobseeker=jobseeker)
        return chat_id

    @staticmethod
    def get_recipient_name(user_id):
        '''get name of recipient'''
        user = User.objects.get(id=user_id)
        if user.user_type == 'jobseeker':
            return JobSeeker.objects.get(user=user).first_name + ' ' + JobSeeker.objects.get(user=user).last_name
        else:
            return Employer.objects.get(user=user).company_name

    @staticmethod
    def get_sender_context(user_id):
        '''get senders data'''
        return User.objects.get(id=user_id)
    
    @staticmethod
    def get_chat_list(user_id):
        '''get list of chats'''
        user=User.objects.get(id=user_id)
        if user.user_type=='company':
            return ChatRoom.objects.filter(employer=Employer.objects.get(user=user))
        else:
            return ChatRoom.objects.filter(jobseeker=JobSeeker.objects.get(user=user))
    
    @staticmethod
    def get_sender_name(sender):
        '''get name of sender'''
        if JobSeeker.objects.filter(user_id=sender).exists():
            sender= JobSeeker.objects.get(user_id=sender)
            sender_name = sender.first_name + sender.last_name
        else:
            sender_name = Employer.objects.get(user_id=sender).company_name
        return sender_name
    
    @staticmethod
    def block_user(request, user_id):
        '''add user to block list'''
        user = request.user
        blocked_user=User.objects.get(id = user_id)
        if BlockList.objects.filter(user=user).exists():
            if blocked_user in BlockList.objects.get(user=user).blocked_user.all():
                pass
            else:
                BlockList.objects.get(user=user).blocked_user.set([blocked_user])
        else:
            block_list = BlockList.objects.create(user=user)
            block_list.blocked_user.set([blocked_user])
    
    @staticmethod
    def unblock_user(request, user_id):
        '''delete user from block list'''
        user = request.user
        blocked_user=User.objects.get(id = user_id)
        BlockList.objects.get(user=user).blocked_user.remove(blocked_user)
    
    @staticmethod
    def is_blocked(recipient_id,user_id):
        '''
        check users block status
        0 - chat is active
        1 - the user has blocked the interlocutor 
        2 - The user has been blocked
        '''
        user = User.objects.get(id = user_id)
        recipient = User.objects.get(id = recipient_id)
        if BlockList.objects.filter(user=user).exists():
            if recipient in BlockList.objects.get(user=user).blocked_user.all():
                return 1
            else:
                return 0
        elif BlockList.objects.filter(user=recipient).exists():
            if user in BlockList.objects.get(user=recipient).blocked_user.all():
                return 2
            else:
                return 0
        else:
            return 0