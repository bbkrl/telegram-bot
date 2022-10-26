import logging
# import os
#
from decouple import config
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tg_bot.settings')
#
import telebot
# from telebot.types import Message
# import django
#
# django.setup()
#
# from bot.bot import Bot
from bot.handlers.handler_main import HandlerMain
#
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

# token = config('TOKEN')
# tb: telebot.TeleBot = telebot.TeleBot(token)

# handler = HandlerMain(tb)

# @tb.message_handler()
# def start_message(message: Message):
#     bot = Bot(message.from_user.id, tb)
#     bot.process_message(message)


class TelBot:
    def __init__(self):
        """
        Инициализация бота
        """
        # получаем токен
        self.token = config('TOKEN')

        # инициализируем бот на основе зарегистрированного токена
        self.bot = telebot.TeleBot(self.token)
        # инициализируем оброботчик событий
        self.handler = HandlerMain(self.bot)
        self.logger = telebot.logger
        telebot.logger.setLevel(logging.DEBUG)

    def start(self):
        """
        Метод предназначен для старта обработчика событий
        """
        self.handler.handle()

    def run_bot(self):
        """
        Метод запускает основные события сервера
        """
        # обработчик событий
        self.start()
        # служит для запуска бота (работа в режиме нон-стоп)
        self.bot.infinity_polling()


if __name__ == '__main__':
    # tb.infinity_polling()
    bot = TelBot()
    bot.run_bot()
