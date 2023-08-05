import json

VIDEOS_DIR = "videos/"
AUDIOS_DIR = "audios/"

with open("utils/lang.json", "r", encoding="utf-8") as lang_file:
    lang = json.load(lang_file)
