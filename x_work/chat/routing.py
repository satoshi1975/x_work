from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<chat_id>\w+)/$", consumers.ChatConsumer.as_asgi()),
    # re_path(r"ws/chat/(?P<chat_id>\w+)/(?P<sender>\w+)/(?P<recipient>\w+)/$", consumers.ChatConsumer.as_asgi()),

]