from telebot.types import Message
from telebot import TeleBot


from bot.states import make_state
from bot.storage import StateStorage


class Bot:
    def __init__(self, user_tg_id: int, tb: TeleBot):
        self.storage = StateStorage(user_tg_id)
        self.state = None
        self.user_tg_id = user_tg_id
        self.tb = tb

    def process_message(self, message: Message):
        state, context = self.storage.get_bot_state()
        self.state = make_state(
            state, context,
            self.storage,
            self.user_tg_id,
            self.tb
        )
        message = self.state.process_message(message)
        return message
