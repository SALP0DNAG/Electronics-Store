from django.db import models
from users import models as u_models
from Store import models as s_models
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Наличными'),
        ('card', 'Картой'),
    ]
    STATUS_CHOICES = [
        ('accept', 'Принят'),
        ('collect', 'В сборке'),
        ('on_the_way', 'В пути'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]
    DELIVERY_CHOICES = [
        ('courier', 'Курьер (Доставка курьером)'),
        ('pickup', 'Самовывоз (На пункте выдачи)'),
    ]

    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    user = models.ForeignKey(u_models.User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cash')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='accept')
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default='pickup')
    address = models.TextField(max_length=250, blank=False)
    comment = models.TextField(max_length=250, blank=True)
    recipient = models.CharField(max_length=100, blank=False)
    phone_number = PhoneNumberField(unique=False, blank=True)

    def __str__(self):
        return f'Order {self.id} by {self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(s_models.Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} | {self.product.name}'

    def get_total_price(self):
        return self.product.price * self.quantity
