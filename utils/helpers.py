from loader import bot
from db.db import PgConn
from keyboard.keyboard import language_buttons


def choose_lang(message):
    try:
        db_conn = PgConn()
        bot.send_message(message.chat.id, f"🇺🇿 Assalomu alaykum, {message.from_user.username}. Tilni tanlang!\n\n"
                                          f"🇷🇺 Здравствуйте, {message.from_user.username}. Выберите язык!\n\n"
                                          f"🇬🇧 Hello, {message.from_user.username}. Choose language!\n\n",
                         reply_markup=language_buttons(message))
        # if get_user_temp(message) == 'no':
        #     bot.send_message(message.from_user.id, f"{emoji.emojize(':Uzbekistan:')} Tilni tanlang!\n\n"
        #                                            f"{emoji.emojize(':Russia:')} Выберите язык!\n\n"
        #                                            f"{emoji.emojize(':United_Kingdom:')} Choose language!\n\n",
        #                      reply_markup=language_buttons(message, get_user_temp(message)))
        # elif get_user_temp(message) == 'some_lang':
        #     bot.register_next_step_handler(message, menu)
        #     bot.send_message(message.from_user.id, f"{lang[get_user_lang(message)]['Choose_lang']}",
        #                      reply_markup=language_buttons(message, get_user_temp(message)))
        # else:
        #     bot.send_message(message.from_user.id, f"{lang[get_user_lang(message)]['Choose_lang']}",
        #                      reply_markup=language_buttons(message, get_user_temp(message)))
    except Exception as e:
        print(e)
