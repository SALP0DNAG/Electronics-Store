from django.db import models
from users import models as md


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.category}"


class SpecialProducts(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='special_products_images')

    def __str__(self):
        return f"SPECIAL {self.category}"


class Characteristics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
    guarantee = models.PositiveIntegerField(verbose_name="Гарантия", blank=True, null=True)
    thread_diameter = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Диаметр резьбы", blank=True)
    material = models.CharField(max_length=30, verbose_name="Материал", blank=True)
    mounting_method = models.CharField(max_length=30, verbose_name="Способ монтажа", blank=True)
    purpose_mixer = models.CharField(max_length=50, verbose_name="Назначение смесителя", blank=True)
    mixer_type = models.CharField(max_length=50, verbose_name="Тип смесителя", blank=True)
    type_liner = models.CharField(max_length=50, verbose_name="Тип подводки", blank=True)
    width = models.PositiveIntegerField(verbose_name="Ширина", blank=True, null=True)
    length = models.PositiveIntegerField(verbose_name="Длина", blank=True, null=True)
    weight = models.PositiveIntegerField(verbose_name="Вес", blank=True, null=True)
    height = models.PositiveIntegerField(verbose_name="Высота", blank=True, null=True)
    wear_resistance = models.CharField(max_length=20, verbose_name="Износостойкость", blank=True)
    country = models.CharField(max_length=20, verbose_name="Страна производитель", blank=True)
    basis = models.CharField(max_length=20, verbose_name="Основа", blank=True)
    color = models.CharField(max_length=20, verbose_name="Цвет", blank=True)
    putty_type = models.CharField(max_length=20, verbose_name="Тип шпатлёвки", blank=True)
    drying_time = models.PositiveIntegerField(verbose_name="Время высыхания", blank=True, null=True)
    volume = models.PositiveIntegerField(verbose_name="Объём", blank=True, null=True)
    thickness = models.PositiveIntegerField(verbose_name="Толщина", blank=True, null=True)
    glass_package = models.CharField(max_length=30, verbose_name="Стеклопакет", blank=True)

    def __str__(self):
        return f"Характеристики для товара {self.product.name}"


class Basket(models.Model):
    user = models.ForeignKey(md.User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}, {self.quantity} штук'

    def sum(self):
        return self.quantity * self.product.price


class Favorite(models.Model):
    user = models.ForeignKey(md.User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
