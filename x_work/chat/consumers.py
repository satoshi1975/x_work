import json
from chat import services,redis_db_manager
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    
    
    async def connect(self):
        
        self.room_name = self.scope["url_route"]["kwargs"]["chat_id"]

        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        messages = await redis_db_manager.get_messages(self.room_name)
        for message in messages:
            await self.send(text_data=json.dumps({"message": message["message_text"]}))



    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        text_data_json = json.loads(text_data)

        message = text_data_json["message"]
        chat_id=text_data_json['chat_id']
        user_id=text_data_json['sender']
        await redis_db_manager.handle_new_message(chat_id, message, user_id)
        await redis_db_manager.get_messages(chat_id)
        # Send message to room group
        print(text_data_json['sender'])
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'user_id':user_id}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event['user_id']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, 'user_id':sender}))
        