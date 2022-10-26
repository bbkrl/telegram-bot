# импортируем класс родитель
from .handler import Handler
# импортируем сообщения пользователю
from bot.message import MESSAGES

from ..models import Order


class HandlerInlineQuery(Handler):
    """
    Класс обрабатывает входящие текстовые
    сообщения от нажатия на инлайн-кнопоки
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_product(self, call, code):
        """
        Обрабатывает входящие запросы на нажатие inline-кнопок товара
        """
        # создаем запись в БД по факту заказа
        self.BD._add_orders(1, code, 1)

        self.bot.answer_callback_query(
            call.id,
            MESSAGES['product_order'].format(
                self.BD.select_single_product_name(code),
                self.BD.select_single_product_title(code),
                self.BD.select_single_product_price(code),
                self.BD.select_single_product_quantity(code)),
            show_alert=True)

    def handle(self):
        # обработчик(декоратор) запросов от нажатия на кнопки товара.
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            code = call.data
            if code.isdigit():
                code = int(code)

            self.pressed_btn_product(call, code)

def _add_orders(qty, product_id, user_id):

    all_id_product = Order.product.all()

    if product_id in all_id_product:
        qty_order = select_order_quantity(product_id)
        qty_order += 1


def select_order_quantity(product_id):
    """
    Возвращает количество товара в заказе
    """
    res = Order.qty.filter(product=product_id).first
    return res

def update_order_value(product_id, name, value):
    pass
