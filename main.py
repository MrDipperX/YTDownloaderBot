import os
from utils.constants import VIDEOS_DIR, AUDIOS_DIR
from loader import bot


if __name__ == '__main__':
    if not os.path.isdir(VIDEOS_DIR):
        os.makedirs(VIDEOS_DIR)
    if not os.path.isdir(AUDIOS_DIR):
        os.makedirs(AUDIOS_DIR)

    bot.polling(none_stop=True)
