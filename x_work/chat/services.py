from main.models import User
from chat.models import ChatRoom
from uuid import uuid4

class ChatManager:
    

    # @staticmethod
    # def generate_chat_id():
       
    #     return uuid4()
    @staticmethod
    def create_chat(user1, user2_id):
        user2=User.objects.get(id=user2_id)
        # print(user1)
        # print(user2)
        chat_id=uuid4().int
        chat=ChatRoom.objects.create(user1=user1,user2=user2,chat_id=chat_id)
        return chat.id



    @staticmethod
    def get_chat_id(user1,user2_id):
        user2=User.objects.get(id=user2_id)
        try:
            chat=ChatRoom.objects.get(user1=user1,user2=user2)
            return chat.chat_id
        
        except:
            chat_id=ChatManager().create_chat(user1,user2_id)
            return chat_id
