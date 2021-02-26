from django.db import models
from shop.models import Product


class Order(models.Model):
    '''Модель для заказа'''
    first_name = models.CharField(verbose_name='Имя',max_length=50, default='')
    last_name = models.CharField(verbose_name='Имя', max_length=50, default='')
    email = models.EmailField(verbose_name='Email',null=True)
    address = models.CharField(verbose_name='Адрес', max_length=250, null=True)
    postal_code = models.CharField(verbose_name='Почтовый индекс',max_length=20, null=True)
    city = models.CharField(verbose_name='Город', max_length=100, null=True)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name='Изменен', auto_now=True)
    paid = models.BooleanField( verbose_name='Статус оплаты', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    '''Модель для показа товаров в заказе'''
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество',default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
