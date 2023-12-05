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
