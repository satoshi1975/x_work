import redis
import json

redis_conn = redis.Redis()



async def get_messages(chat_id):

    # r = redis.Redis(host='localhost', port=6379, db=0)
    # chat_key = f"chat:{chat_id}:messages"
    # messages = r.lrange(chat_key, 0, -1)  # Получение всех сообщений из списка
    # parsed_messages = []
    # for message_json in messages:
    #     message_data = json.loads(message_json)
    #     sender_id = message_data.get("sender_id")
    #     message_text = message_data.get("message_text")
    #     parsed_message = f"ID отправителя: {sender_id}\nСообщение: {message_text}"
    #     parsed_messages.append(parsed_message)
    # return parsed_messages
    r = redis.Redis(host='localhost', port=6379, db=0)
    chat_key = f"chat:{chat_id}:messages"
    messages = r.lrange(chat_key, 0, -1)  # Получение всех сообщений из списка
    parsed_messages = []
    for message_json in messages:
        message_data = json.loads(message_json)
        parsed_messages.append({
            "sender_id": message_data.get("sender_id"),
            "message_text":f'{message_data.get("sender_id")} : {message_data.get("message_text")}'
        })
    return parsed_messages


    # print('asfasfaffffffffffffffffffffffffff')
    # r = redis.Redis(host='localhost', port=6379, db=0)
    # chat_key = f"chat:{chat_id}"
    # messages = r.hgetall(chat_key)
    # parsed_messages = []
    # for message_id, message_json in messages.items():
    #     message_data = json.loads(message_json)
    #     sender_id = message_data.get("sender_id")
    #     message_text = message_data.get("message_text")
    #     parsed_messages.append({
    #         "message_id": message_id.decode(),  # Преобразование типа bytes в str
    #         "sender_id": sender_id,
    #         "message_text": message_text
    #     })
    # print(parsed_messages)
    # return parsed_messages


    # Установка соединения с Redis
    # r = redis.Redis(host='localhost', port=6379, db=0)

    # # Создание ключа чата в формате "chat:<chat_id>"
    # chat_key = f"chat:{chat_id}"

    # # Получение всех сообщений из Redis
    # messages = r.hgetall(chat_key)

    # # Парсинг и вывод сообщений
    # for message_id, message_json in messages.items():
    #     message_data = json.loads(message_json)
    #     sender_id = message_data.get("sender_id")
    #     message_text = message_data.get("message_text")
    #     print(f"ID сообщения: {message_id}")
    #     print(f"Отправитель: {sender_id}")
    #     print(f"Текст сообщения: {message_text}")
    #     print("---")





async def handle_new_message(chat_id, message, user_id):

    r = redis.Redis(host='localhost', port=6379, db=0)
    chat_key = f"chat:{chat_id}:messages"  # Измененный ключ для списка сообщений
    message_data = {
        "sender_id": user_id,
        "message_text": message
    }
    message_json = json.dumps(message_data)
    # Добавление сообщения в конец списка
    r.rpush(chat_key, message_json)


    # print(type(chat_id))
    # print(type(message))
    # print(type(user_id))
    # r = redis.Redis(host='localhost', port=6379, db=0)

    # chat_key = f"chat:{chat_id}"

    # # Создание уникального идентификатора сообщения
    # message_id = r.incr(f"chat:{chat_id}:message_counter")

    # # Формирование данных сообщения
    # message_data = {
    #     "sender_id": user_id,
    #     "message_text": message
    # }
    # message_json = json.dumps(message_data)
    # # Сохранение сообщения в Redis
    # r.hset(chat_key, message_id, message_json)

    # print(f"Сообщение сохранено в чате {chat_id}. ID сообщения: {message_id}, Text:{message_json}" )
    