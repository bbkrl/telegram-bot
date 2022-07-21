from abc import ABCMeta, abstractmethod

from telebot import TeleBot
from telebot.types import Message


class State(metaclass=ABCMeta):
    name = 'abstact'

    @abstractmethod
    def __init__(self, user_tg_id: int, context: dict, storage, tb: TeleBot):
        pass

    @abstractmethod
    def process_message(self, message: Message):
        pass