from telegram.ext import CommandHandler, MessageHandler, ConversationHandler
from telegram.ext import Filters

from conversation_handlers import settings_menu_conversation_handler
from conversation_handlers import editor_menu_conversation_handler

from menu import send_main_menu, send_editor_menu, send_settings_menu

from all_json import KEYBOARDS

from languages import get_user_language
from keyboards import check_button
from tasks import get_today_tasks
from messages import get_message


# Function for send greeting and send main menu fo user
# Used for the command /start
def start_handler(update, context):
    language = get_user_language(update=update, short=True)

    update.message.reply_text(get_message("welcome", language))
    send_main_menu(update)

    return 'main_menu'


# Function - handler for main menu buttons. Buttons:
# today's tasks, editor, settings
def handler(update, context):
    user_id = update.message.from_user.id
    language = get_user_language(user_id=user_id, short=True)

    pushed_button = check_button(
        update, KEYBOARDS["static"]["main_menu"], language
    )

    if pushed_button == "today_tasks":
        today_tasks = get_today_tasks(user_id)

        if today_tasks:
            text = get_message("today_tasks", language) + '\n\n'
            for task in today_tasks:
                text += task.title + "\n"
        else:
            text = get_message("not_tasks_today", language)

        update.message.reply_text(text)

        return "main_menu"

    elif pushed_button == "editor":
        send_editor_menu(update)
        return "editor"

    elif pushed_button == "settings":
        send_settings_menu(update)
        return "settings"

    else:
        update.message.reply_text(get_message("click_buttons", language))
        send_main_menu(update)
        return "main_menu"


# Conversation scheme
main_menu_conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start_handler),
        MessageHandler(Filters.text, handler)
    ],

    states={
        "main_menu": [MessageHandler(Filters.text, handler)],
        "editor": [editor_menu_conversation_handler],
        "settings": [settings_menu_conversation_handler]
    },

    fallbacks=[]
)
