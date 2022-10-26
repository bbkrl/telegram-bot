import abc
from bot.markup.markup import Keyboards


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем разметку кнопок
        self.keybords = Keyboards()

    @abc.abstractmethod
    def handle(self):
        pass
