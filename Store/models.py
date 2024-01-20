from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    guarantee = models.PositiveIntegerField(default=None)
    thread_diameter = models.DecimalField(default=None, max_digits=5, decimal_places=2)
    material = models.CharField(max_length=30, default=None)
    mounting_method = models.CharField(max_length=30, default=None)
    purpose_mixer = models.CharField(max_length=50, default=None)
    mixer_type = models.CharField(max_length=50, default=None)
    type_liner = models.CharField(max_length=50, default=None)
    width = models.PositiveIntegerField(default=None)
    length = models.PositiveIntegerField(default=None)
    weight = models.PositiveIntegerField(default=None)
    height = models.PositiveIntegerField(default=None)
    wear_resistance = models.CharField(max_length=20, default=None)
    country = models.CharField(max_length=20, default=None)
    basis = models.CharField(max_length=20, default=None)
    color = models.CharField(max_length=20, default=None)
    putty_type = models.CharField(max_length=20, default=None)
    drying_time = models.PositiveIntegerField(default=None)
    volume = models.PositiveIntegerField(default=None)
    thickness = models.PositiveIntegerField(default=None)
    glass_package = models.CharField(max_length=30, default=None)

    def __str__(self):
        return f"Характеристики для товара {self.product.name}"

