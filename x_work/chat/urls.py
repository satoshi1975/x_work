from django.urls import path
from . import views

urlpatterns = [
    path("user/<int:user_id>/", views.redirect_to_chat, name='room'), #redirecting to chat with user
    path("my_chats/<int:user_id>/", views.my_chats, name='my_chats'), #list of chats
    path("<str:chat_id>/", views.chat, name="chat"), #display chat
    path("block/<str:user_id>", views.block_user, name="block"), #add user to block list
    path("unblock/<str:user_id>", views.unblock_user, name="unblock"), #delete user from block list
]