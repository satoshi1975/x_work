from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("user/<int:user_id>/", views.redirect_to_chat, name='room'),
    path("my_chats/<int:user_id>/", views.my_chats, name='my_chats'),
    path("<str:chat_id>/", views.chat, name="chat"),
]