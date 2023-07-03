'''chat data menegement'''
import redis
import json

redis_conn = redis.Redis()



async def get_messages(chat_id):
    '''get all messages in chat by chat id'''
    r = redis.Redis(host='localhost', port=6379, db=0)
    chat_key = f"chat:{chat_id}:messages"
    messages = r.lrange(chat_key, 0, -1)  
    parsed_messages = []
    for message_json in messages:
        message_data = json.loads(message_json)
        parsed_messages.append({
            "sender_id": message_data.get("sender"),
            "message_text":f'{message_data.get("sender")} : {message_data.get("message_text")}'
        })
    return parsed_messages


    
async def handle_new_message(chat_id, message, sender):
    '''add new message in chat'''
    r = redis.Redis(host='localhost', port=6379, db=0)
    chat_key = f"chat:{chat_id}:messages"  
    message_data = {
        "sender": sender,
        "message_text": message
    }
    message_json = json.dumps(message_data)
    r.rpush(chat_key, message_json)

    