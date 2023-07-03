import json
from chat import services,redis_db_manager
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from employers.models import Employer
from job_seekers.models import JobSeeker
from chat.services import ChatManager

class ChatConsumer(AsyncWebsocketConsumer):
    
    
    async def connect(self):
        '''connect to chat'''
        self.room_name = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        messages = await redis_db_manager.get_messages(self.room_name)
        for message in messages:
            await self.send(text_data=json.dumps({"message": message["message_text"]}))



    async def disconnect(self, close_code):
        '''hang up on chat'''
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )
    async def receive(self, text_data):
        '''Receive and process a new chat message'''
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        chat_id=text_data_json['chat_id']
        sender_name=text_data_json['sender_name']
        await redis_db_manager.handle_new_message(chat_id, message, sender_name)
        await redis_db_manager.get_messages(chat_id)
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message,'sender_name':sender_name}
        )


    async def chat_message(self, event):
        '''display new message in chat'''
        message = event["message"]
        
        sender_name=event['sender_name']
        await self.send(text_data=json.dumps({"message": message, 'sender_name':sender_name}))
        