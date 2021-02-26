from datetime import datetime

from django.db import models


class Product(models.Model):
    '''
        Модель для товара
    '''
    name = models.CharField(verbose_name='Название', max_length=25)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='products')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Стоимость', max_digits=8, decimal_places=2, null=True)
    image = models.ImageField(verbose_name='Изображение')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    '''
    Модель для категории товара
    '''
    name = models.CharField("Название категории", max_length=150)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Review(models.Model):
    '''Модель для отзывов'''
    text = models.TextField(verbose_name="Текст отзыва", max_length=500)
    item = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name="Имя", max_length=50)
    rating = models.IntegerField(verbose_name="Рейтинг", null=True, blank=True)
    timestamp = models.DateTimeField(verbose_name="Метка времени",default=datetime.now())
    session = models.CharField(verbose_name="Идентиифкатор сессии",max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"