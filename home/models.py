from django.db import models
from django.contrib.auth.models import User

from product.models import Product
from admin_panel.models import UserAddress

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    units = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.user

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
