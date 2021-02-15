from datetime import timezone, datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    image = models.ImageField("Image")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    name = models.CharField("Название категории", max_length=150)
    description = models.TextField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Review(models.Model):
    text = models.TextField("Текст отзыва", max_length=500)
    item = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Имя", max_length=50)
    rating = models.IntegerField("Рейтинг", null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.now())
    session = models.CharField("Идентиифкатор сессии",max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"