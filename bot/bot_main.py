'''Telegram Bot for Embedded Python Project'''

import logging

from telegram import Update
# , MessageHandler, Filters
from telegram.ext import Updater, CommandHandler, CallbackContext

from api_token import TOKEN

HELP = '''
/comando1 - dummy text
/comando2 - dummy text
'''

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start_command(update: Update, context: CallbackContext) -> None:
    '''Responds to /start command'''
    update.message.reply_text(f'Bem vindo {update.message.chat.username}')


def help_command(update: Update, context: CallbackContext) -> None:
    '''Responds to /help command'''
    update.message.reply_text(HELP)


def run():
    '''Starts the bot'''

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))

    updater.start_polling()
    updater.idle()
