import logging
import os

from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tg_bot.settings')

import telebot
from telebot.types import Message
import django
django.setup()

from bot.bot import Bot

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

token = config('TOKEN')
tb: telebot.TeleBot = telebot.TeleBot(token)


@tb.message_handler()
def start_message(message: Message):
    bot = Bot(message.from_user.id, tb)
    bot.process_message(message)


if __name__ == '__main__':
    tb.infinity_polling()
