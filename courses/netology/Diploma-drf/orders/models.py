from django.db import models

from backendAPI.models import Category, Shop
from users.models import User, Contact

STATE_CHOICES = (
    ('cart', 'В корзине'),
    ('new', 'Новый'),
    ('confirmed', 'Подтвержден'),
    ('assembled', 'Собран'),
    ('sent', 'Отправлен'),
    ('delivered', 'Доставлен'),
    ('canceled', 'Отменен'),
)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='shopAPI', blank=True,
                             on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Статус', choices=STATE_CHOICES, max_length=15, default='cart')
    contact = models.ForeignKey(Contact, verbose_name='Контакт', blank=True, null=True,
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Список заказов"
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)
    # return self.created


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='ordered_items', blank=True,
                              on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория товара', blank=True, null=True,
                                 on_delete=models.SET_NULL)
    shop = models.ForeignKey(Shop, verbose_name='магазин', blank=True, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=80, verbose_name='Название товара')
    external_id = models.PositiveIntegerField(verbose_name='Внешний ИД')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    total_amount = models.PositiveIntegerField(default=0, verbose_name='Общая стоимость')

    class Meta:
        verbose_name = 'Заказанная позиция'
        verbose_name_plural = "Список заказанных позиций"
        constraints = [
            models.UniqueConstraint(fields=['order_id', 'product_name'], name='unique_order_item'),
        ]

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.total_amount = self.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)
