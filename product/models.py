from django.db import models
from django.utils.datetime_safe import datetime
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2 )
    discount_price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    units = models.IntegerField()
    cover = models.ImageField(upload_to='covers/%Y/%m/%d', blank=True)
    publish = models.BooleanField(default=True)
    category = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)    

    def __str__(self):
        return self.name

class Category_Parents(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='id', related_name='parent')
    child = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='id', related_name='child')

    def __str__(self):
        return str(self.parent)+' -> '+str(self.child)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)


class Entry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.name)


@receiver(post_save, sender=Entry)
def update_add_cart(sender, instance, **kwargs):
    instance.cart.total = Decimal(instance.cart.total) + Decimal(instance.quantity * instance.product.price)
    instance.cart.count += instance.quantity
    instance.cart.updated = datetime.now()
    instance.cart.save()
