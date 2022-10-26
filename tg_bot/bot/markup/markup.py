from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

from bot.config import KEYBOARD

from bot.models import Category, Product

# from tg_bot.bot.models import Product


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """
    # инициализация разметки

    def __init__(self):
        self.markup = None

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """

        return KeyboardButton(KEYBOARD[name])

    def start_menu(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)

        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')

        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    @staticmethod
    def remove_menu():
        return ReplyKeyboardRemove()

    def category_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('PIZZA'))
        self.markup.add(self.set_btn('BEER'))
        self.markup.add(self.set_btn('HOOKAH'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))

        return self.markup

    @staticmethod
    def set_inline_btn(name):
        """
        Создает и возвращает инлайн-кнопку по входным параметрам
        """
        return InlineKeyboardButton(str(name),
                                    callback_data=str(name.id))

    def set_select_category(self, category):
        """
        Создает разметку инлайн-кнопок в выбранной
        категории товара и возвращает разметку
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        # загружаем в названия инлайн-кнопок данные
        # из БД в соответствие с категорией товара
        # for itm in self.BD.select_all_products_category(category):
        #     self.markup.add(self.set_inline_btn(itm))

        result = list(Product.objects.all().filter(category_id=category))
        print('result', result)
        for itm in result:
            self.markup.add(self.set_inline_btn(itm))

        return self.markup
