from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Data for categories of products"""
    class Meta:
        verbose_name_plural = 'Категории'

    name = models.CharField('Название в структуре сайта', max_length=254)
    friendly_name = models.CharField('Название на сайте', max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """Products data model"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL, help_text="Выберете категорию")
    sku = models.CharField('Артикул:', max_length=254, null=True, blank=True)
    name = models.CharField('Назвaние', max_length=254)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=7, decimal_places=0)
    image_url = models.URLField('Ссылка на изображение:', max_length=1024, null=True, blank=True)
    image = models.ImageField('Изображение:', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def get_rating(self):
        total = sum(int(reviews['stars']) for reviews in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE, help_text="Выберете товар")
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE, help_text="Выберете пользователя")

    content = models.TextField('Текст', blank=True, null=True)
    stars = models.IntegerField('Оценка')

    date_added = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Отзывы на продукцию"
        verbose_name = "Отзыв"