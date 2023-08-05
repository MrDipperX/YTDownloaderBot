from loader import bot
from db.db import PgConn
import os
from utils.yt_downloader import available_resolutions, downloader_audio, downloader_video
from keyboard.keyboard import choose_resolution
from utils.constants import lang


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    try:
        db_conn = PgConn()
        some_data = db_conn.get_user_info(call.message.chat.id)
        resolutions = available_resolutions(some_data[2])

        if call.data == "video":
            bot.edit_message_text(lang[db_conn.get_user_lang(call.message.chat.id)]['Choose_resolution'],
                                  call.message.chat.id, call.message.message_id,
                                  reply_markup=choose_resolution(call.message, some_data[2]))
            db_conn.set_content_type(call.message.chat.id, 'video')

        elif call.data == "audio":
            wait_mess = bot.edit_message_text(f"{lang[db_conn.get_user_lang(call.message.chat.id)]['Wait']}...",
                                              call.message.chat.id, call.message.message_id)
            db_conn.set_content_type(call.message.chat.id, 'audio')
            audio_path, audio_title = downloader_audio(some_data[2])
            bot.send_audio(call.message.chat.id, open(audio_path, 'rb'), caption=audio_title)
            bot.delete_message(call.message.chat.id, wait_mess.message_id)
            os.remove(audio_path)

        elif call.data in resolutions:
            wait_mess = bot.edit_message_text(f"{lang[db_conn.get_user_lang(call.message.chat.id)]['Wait']}...",
                                              call.message.chat.id, call.message.message_id)
            video_path, video_title = downloader_video(some_data[2], quality=call.data)
            bot.send_document(call.message.chat.id, open(video_path, 'rb'), caption=video_title)
            bot.delete_message(call.message.chat.id, wait_mess.message_id)
            os.remove(video_path)

    except Exception as e:
        print(e)
