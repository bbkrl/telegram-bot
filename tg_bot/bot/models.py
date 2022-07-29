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
    desctiption = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ManyToManyField('Category', on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Category(models.Model):
    class Meta:
        db_table = 'Category'

    name = models.CharField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)


class Order(models.Model):
    class Meta:
        db_table = 'Order'

    qty = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    product = models.ManyToManyField(Product, on_delete=models.CASCADE, related_name='orders')
    user_id = models.IntegerField()
