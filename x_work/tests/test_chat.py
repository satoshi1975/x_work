from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
from django.test import TestCase
from django.urls import reverse
from main.models import User, Cities
import json
from job_seekers.models import JobSeeker
from employers.models import Employer
from datetime import date
from chat.consumers import ChatConsumer



class ChatConsumerTestCase(TestCase):
    async def test_chat_message(self):
        # data = {'url_route':{'kwargs':{'chat_id':'12345678'}}}
        communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/ws/")
        communicator.scope["url_route"] = {
                                        "kwargs": {
                                            "chat_id": "12345"  
                                        }
                                            }
        connected, _ = await communicator.connect()

        # Отправить сообщение через WebSocket
        await communicator.send_json_to({"message": "Hello, world!", "sender_name": "John",'chat_id':'12345'})

        # Получить сообщение с WebSocket
        response = await communicator.receive_json_from()

        # Проверить полученные данные
        self.assertEqual(response["message"], "Hello, world!")
        self.assertEqual(response["sender_name"], "John")

        await communicator.disconnect()

    async def test_handle_new_message(self):
        # Подготовить данные для теста
        chat_id = "room1"
        message = "Hello, world!"
        sender_name = "John"
        data = {
            "type": "chat_message",
            "message": message,
            "sender_name": sender_name,
        }

        # Создать экземпляр Consumer
        consumer = ChatConsumer()

        # Подключить Consumer к каналу
        channel_layer = get_channel_layer()
        await channel_layer.send(f"chat_{chat_id}", data)

        # Получить ответ от Consumer
        response = await channel_layer.receive(f"chat_{chat_id}")

        # Проверить полученные данные
        self.assertEqual(response["type"], "chat_message")
        self.assertEqual(response["message"], message)
        self.assertEqual(response["sender_name"], sender_name)

# class ConnectionTestCase(TestCase):
    
#     def setUp(self):
#         self.city = Cities.objects.create(city='New York', state_name='New York')
#         self.user = User.objects.create(email='testuser@gos.com', password='testpassword', username='testuser1',user_type='company')
#         self.user2 = User.objects.create(email='testuser2@gos.com', password='testpassword', username='testuser2',user_type='jobseeker')
#         self.jobseeker = JobSeeker.objects.create(user=self.user2,first_name='user2',last_name='user2',
#                                                 date_of_birth=date.today(),phone_number='123',city=self.city,email='test@test.com')
#         self.employer = Employer.objects.create(user=self.user,company_info='info',company_name='test',industry='info',
#                                                 email='test@test.com',phone_number='123',website='www.test.com',city=self.city)
#     def test_conn(self):
#         self.client.force_login(self.user)
#         response = self.client.get(reverse('room',kwargs={'user_id':self.user2.id}))
#         print(response.url)