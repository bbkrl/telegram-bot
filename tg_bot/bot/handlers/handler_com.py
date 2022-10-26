from .handler import Handler


class HandlerCommands(Handler):
    def __int__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' здравствуйте! Жду дальнейших задач.',
                              reply_markup=self.keybords.start_menu())

    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие /start команды.
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(type(message))
            if message.text == '/start':
                self.pressed_btn_start(message)
