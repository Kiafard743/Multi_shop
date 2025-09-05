from django.db import models
from account.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.SmallIntegerField()

    def __str__(self):
        return self.order.phone


class DiscountCode(models.Model):
    name = models.CharField(max_length=100, unique=True)
    discount = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name
