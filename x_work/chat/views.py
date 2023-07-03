from django.shortcuts import render,redirect
from chat.services import ChatManager
from django.urls import reverse
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required


@login_required
def my_chats(request, user_id):
    '''a view of all the user's chats'''
    chat_list=ChatManager().get_chat_list(user_id) 
    sender=ChatManager().get_sender_context(user_id)
    chat=chat_list.first()
    chat_id=chat.chat_id
    if request.user.user_type == 'company':
        recipient=chat.jobseeker
    else:
        recipient=chat.employer

    return render(request, "chat.html", {"chat_id": chat_id, 'user_id':user_id,
                                        'recipient':recipient,'chat_list':chat_list})

@login_required
def redirect_to_chat(request, user_id):
    '''redirecting to chat with user by user id view'''
    if request.user.user_type == 'company':
        chat_id=ChatManager().get_chat_id(employer_id=request.user.id, jobseeker_id=user_id)
    else:
        chat_id=ChatManager().get_chat_id(jobseeker_id=request.user.id,employer_id=user_id)
    if chat_id == False:
        previous_page = request.META.get('HTTP_REFERER')
        return redirect(previous_page)
    url_chat=reverse('chat',kwargs={'chat_id':chat_id})
    kwargs={'recipient_id': user_id}
    url_chat += f'?{urlencode(kwargs)}'
    return redirect(url_chat)


@login_required
def chat(request, chat_id):
    '''display chat with user'''
    user_id=request.user.id
    recipient_id=request.GET.get('recipient_id')
    
    recipient=ChatManager().get_recipient_name(recipient_id)
    sender=ChatManager().get_sender_context(user_id)
    chat_list=ChatManager().get_chat_list(user_id)
    sender_name=ChatManager().get_sender_name(user_id)
    is_blocked = ChatManager().is_blocked(recipient_id,user_id)
    return render(request, "chat.html",
                    {"chat_id": chat_id, 'user_id':user_id,'recipient':recipient,'recipient_id':recipient_id,
                    'chat_list':chat_list, 'sender_name':sender_name, 'is_blocked':is_blocked})
    
@login_required
def block_user(request, user_id):
    '''add user to block list'''
    ChatManager().block_user(request,user_id)
    previous_page = request.META.get('HTTP_REFERER')
    return redirect(reverse('room',kwargs={'user_id':user_id}))

@login_required
def unblock_user(request, user_id):
    '''delete user from block list'''
    ChatManager().unblock_user(request,user_id)
    previous_page = request.META.get('HTTP_REFERER')
    return redirect(reverse('room',kwargs={'user_id':user_id}))
   
    