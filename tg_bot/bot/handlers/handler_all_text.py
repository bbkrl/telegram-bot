# # импортируем ответ пользователю
# from bot.messages import MESSAGES
# from bot import config
# # импортируем класс-родитель
# from .handler import Handler
#
#
# class HandlerAllText(Handler):
#     """
#     Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
#     """
#
#     def __init__(self, bot):
#         super().__init__(bot)
#
#         # шаг в заказе
#         self.step = 0
#
#     def pressed_btn_info(self, message):
#         self.bot.send_message(message.chat.id,
#                               MESSAGES['trading_store'],
#                               parse_mode='HTML',
#                               reply_markup=self.keybords.info_menu()
#                               )
#
#     def pressed_brn_settings(self, message):
#         self.bot.send_message(message.chat.id,
#                               MESSAGES=['settings'],
#                               parse_mode='HTML',
#                               reply_markup=self.keybords.settings_menu()
#                               )
#
#     def pressed_btn_back(self, message):
#         self.bot.send_message(message.chat.id,
#                               'Вы вернулись назад',
#                               reply_markup=self.keybords.start_menu()
#                               )
#
#         def handle(self):
#             @self.bot.message_handler(func=lambda message: True)
#             def handle(self):
#                 # ********** меню ********** #
#
#                 if message.text == config.KEYBOARD['INFO']:
#                     self.pressed_btn_info(message)
#
#                 if message.text == config.KEYBOARD['SETTINGS']:
#                     self.pressed_btn_settings(message)
#
#                 if message.text == config.KEYBOARD['<<']:
#                     self.pressed_btn_back(message)
#

# импортируем ответ пользователю
from bot.messages import MESSAGES
from bot import config
# импортируем класс-родитель
from .handler import Handler


class HandlerAllText(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)
        # шаг в заказе
        self.step = 0

    def pressed_btn_info(self, message):
        """
        обрабатывает входящие текстовые сообщения
        от нажатия на кнопоку 'О магазине'.
        """
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.info_menu())

    def pressed_btn_settings(self, message):
        """
        обрабатывает входящие текстовые сообщения
        от нажатия на кнопоку 'Настройки'.
        """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.settings_menu())

    def pressed_btn_back(self, message):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку 'Назад'.
        """
        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keybords.start_menu())

    def pressed_btn_category(self, message):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'. А точне
        это выбор категории товаров
        """
        self.bot.send_message(message.chat.id, "Каталог категорий товара",
                              reply_markup=self.keybords.remove_menu())
        self.bot.send_message(message.chat.id, "Сделайте свой выбор",
                              reply_markup=self.keybords.category_menu())

    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** меню ********** #

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

