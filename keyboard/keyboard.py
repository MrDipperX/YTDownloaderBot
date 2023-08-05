from telebot import types
from utils.yt_downloader import available_resolutions


def choose_video_or_audio(message):
    inline_markup = types.InlineKeyboardMarkup()
    video = types.InlineKeyboardButton('video', callback_data='video')
    audio = types.InlineKeyboardButton('audio', callback_data='audio')
    inline_markup.add(video, audio)

    return inline_markup


def choose_resolution(message, link):
    resolutions = []
    inline_markup = types.InlineKeyboardMarkup()
    for res in available_resolutions(link):
        resolutions.append(types.InlineKeyboardButton(f'{res}', callback_data=f'{res}'))
    inline_markup.add(*resolutions)

    return inline_markup


def language_buttons(message, user_temp='no'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    uz_btn = types.KeyboardButton(f"🇺🇿 O'zbekcha")
    ru_btn = types.KeyboardButton(f"🇷🇺 Русский")
    en_btn = types.KeyboardButton(f"🇬🇧 English")
    keyboard.add(uz_btn, ru_btn, en_btn)
    # if user_temp not in ['no', 'some_lang']:
    #     back_btn = types.KeyboardButton(f"{emoji.emojize(':left_arrow:')} "
    #                                     f"{lang[get_user_lang(message)]['Back_btn']}")
    #     keyboard.add(back_btn)
    return keyboard
