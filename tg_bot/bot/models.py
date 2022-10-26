# from itertools import product
from itertools import product

from django.db import models


class BotState(models.Model):
    class Meta:
        db_table = 'BotState'

    user_tg_id = models.BigIntegerField(
        unique=True,
        db_index=True,
    )

    state_name = models.CharField(
        max_length=255
    )

    context = models.JSONField(default=dict)


class Product(models.Model):
    class Meta:
        db_table = 'Product'

    product_name = models.CharField(max_length=255, db_index=True)
    brand_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product_name)


class Category(models.Model):
    class Meta:
        db_table = 'Category'

    name = models.CharField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    class Meta:
        db_table = 'Order'

    qty = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    user_id = models.IntegerField()

    def select_All_product_id(self):
        result = Order.product.all()
        prod = Product()
        res = prod.orders.all()

        ress = Product.get

    def select_order_quantity(self, product_id):
        """
        Возвращает количество товара в заказе
        """
        res = Order.qty.filter
        result = self._session.query(Order.quantity).filter_by(
            product_id=product_id).one()
        self.close()
        return result.quantity

    def _add_orders(self, qty, product_id, user_id):
        all_id_product = product.orders.all()
