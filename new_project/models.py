from django.db import models

# Create your models here


class Product(models.Model):

    product_name = models.CharField(max_length=100, verbose_name='Название')
    product_desc = models.CharField(max_length=1000, verbose_name='Описание')
    product_pic = models.ImageField(verbose_name='Картинка', null=True, blank=True)
    product_cat = models.CharField(max_length=100, verbose_name='Категория')
    product_price = models.IntegerField(verbose_name='Цена')
    product_mk = models.CharField(max_length=100, verbose_name='Дата создания')
    product_ed = models.CharField(max_length=100, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.product_name} {self.product_price} {self.product_cat}'

    class Meta:
        verbose_name = 'Продукты'
        ordering = ('id',)


class Category(models.Model):

    category_name = models.CharField(max_length=100, verbose_name='Название')
    category_desc = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категории'
        ordering = ('id',)
