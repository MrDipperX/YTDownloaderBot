from loader import bot
from db.db import PgConn
from utils.constants import lang
from keyboard.keyboard import choose_video_or_audio


@bot.message_handler(content_types=['text'])
def mess(message):
    db_conn = PgConn()
    try:
        get_message_bot = message.text.strip()

        if 'https' in get_message_bot:
            if 'https://www.youtube.com/watch' or 'https://www.youtube.com/shorts' in get_message_bot:
                db_conn.set_last_link(message.chat.id, get_message_bot)
                bot.send_message(message.chat.id, lang[db_conn.get_user_lang(message.chat.id)]['Please_choose'],
                                 reply_markup=choose_video_or_audio(message))
            else:
                bot.reply_to(message, lang[db_conn.get_user_lang(message.chat.id)]['Not_yt_link'])

        elif get_message_bot in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"]:
            if get_message_bot == "🇺🇿 O'zbekcha":
                db_conn.set_user_lang("uz", message.from_user.id)

            elif get_message_bot == "🇷🇺 Русский":
                db_conn.set_user_lang("ru", message.from_user.id)

            elif get_message_bot == "🇬🇧 English":
                db_conn.set_user_lang("en", message.from_user.id)

            bot.send_message(message.chat.id, lang[db_conn.get_user_lang(message.chat.id)]['Send_me_link'],
                             reply_markup=None)

    except Exception as e:
        print(e)