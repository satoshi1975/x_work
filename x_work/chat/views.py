from django.shortcuts import render,redirect
from chat.services import ChatManager
from django.urls import reverse
from chat.services import ChatManager

def index(request):
    return render(request, "index.html")


def redirect_to_chat(request, user_id):
    
    chat_id=ChatManager().get_chat_id(request.user, user_id)
    url_chat=reverse('chat',kwargs={'chat_id':chat_id})
    return redirect(url_chat)

def chat(request, chat_id):
    print(request)
    user_id=request.user.id

    return render(request, "chat.html", {"chat_id": chat_id, 'user_id':user_id})
    