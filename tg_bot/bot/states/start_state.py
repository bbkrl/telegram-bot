from telebot import types
from telebot import TeleBot

from .abstract import State


class StartState(State):
    def __init__(self, user_tg_id, context, storage, tb: TeleBot):
        self.context = context
        self.storage = storage
        self.user_tg_id = user_tg_id
        self.tb = tb

    def process_message(self, message: types.Message) -> str:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        start_order_btn = types.KeyboardButton('Start Order')
        markup.add(start_order_btn)

        self.tb.send_message(
            message.chat.id,
            f'Привет {message.from_user.first_name}! Хотите сделать заказ?',
            reply_markup=markup,
        )
