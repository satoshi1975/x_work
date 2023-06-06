import redis

redis_conn = redis.Redis()

async def get_chat_messages(chat_id):
    # Получение всех сообщений из Redis по идентификатору чата
    messages = redis_conn.lrange(chat_id, 0, -1)
    return messages


async def handle_new_message(chat_id, message):
    # Сохранение сообщения в Redis
    redis_conn.rpush(chat_id, message)

    # Дополнительная логика, если необходимо