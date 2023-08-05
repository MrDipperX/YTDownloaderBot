from loader import bot
from db.db import PgConn
from utils.helpers import choose_lang


@bot.message_handler(commands=['start'])
def start(message):
    try:
        db_conn = PgConn()
        db_conn.create_tables()
        db_conn.add_user(message.chat.id, message.from_user.username)
        choose_lang(message)

    except Exception as e:
        print(e)