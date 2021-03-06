"""Module for json file opening"""

import json

SETTINGS = json.load(open("json/settings.json", encoding="utf8"))
KEYBOARDS = json.load(open("json/keyboards.json", encoding="utf8"))
BUTTONS = json.load(open("json/buttons.json", encoding="utf8"))
MESSAGES = json.load(open("json/messages.json", encoding="utf8"))
LANGUAGES = json.load(open("json/languages.json", encoding="utf8"))
SIGNBOARDS = json.load(open("json/signboards.json", encoding="utf8"))
DAYS_OF_THE_WEEK = json.load(
    open("json/days_of_the_week.json", encoding="utf8")
)
