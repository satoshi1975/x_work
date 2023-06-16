from django.shortcuts import render,redirect
from chat.services import ChatManager
from django.urls import reverse
from chat.services import ChatManager
from urllib.parse import urlencode

def index(request):
    return render(request, "index.html")


def my_chats(request, user_id):
    chat_list=ChatManager().get_chat_list(user_id)
    sender=ChatManager().get_sender_context(user_id)
    chat=chat_list.first()
    chat_id=chat.chat_id
    if request.user.user_type == 'company':
        recipient=chat.jobseeker
    else:
        recipient=chat.employer

        

    return render(request, "chat.html", {"chat_id": chat_id, 'user_id':user_id,'recipient':recipient,'chat_list':chat_list})


def redirect_to_chat(request, user_id):
    if request.user.user_type == 'company':
        chat_id=ChatManager().get_chat_id(employer_id=request.user.id, jobseeker_id=user_id)
    else:
        chat_id=ChatManager().get_chat_id(jobseeker_id=request.user.id,employer_id=user_id)

    # recipient=ChatManager().get_recipient_conext(user_id)
    url_chat=reverse('chat',kwargs={'chat_id':chat_id})
    kwargs={'recipient_id': user_id}
    url_chat += f'?{urlencode(kwargs)}'
    return redirect(url_chat)



def chat(request, chat_id):
    user_id=request.user.id
    recipient_id=request.GET.get('recipient_id')
    
    recipient=ChatManager().get_recipient_context(recipient_id)
    sender=ChatManager().get_sender_context(user_id)
    chat_list=ChatManager().get_chat_list(user_id)

    
    return render(request, "chat.html", {"chat_id": chat_id, 'user_id':user_id,'recipient':recipient,'chat_list':chat_list})
    