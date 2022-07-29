from .handler_com import HandlerCommands
from .handler_all_text import HandlerAllText

class HandlerMain:
    """
    Класс компоновщик
    """
    def __init__(self, bot):
        # получаем нашего бота
        self.bot = bot
        # здесь будет иницаилизация обработчиков
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)

    def handle(self):
        # здесь будет запуск обработчиков
        self.handler_commands.handle()
        self.handler_all_text.handle()
