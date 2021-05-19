from django.contrib.auth.models import User
from decimal import Decimal
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.datetime_safe import datetime

from product import models as product_models


# @receiver(post_save, sender=User)
# def add_cart(sender,instance, **kwargs):
#     product_models.Cart.objects.create(user=instance)

@receiver(post_save, sender=product_models.Entry)
def update_add_cart(sender, instance, **kwargs):
    instance.cart.total = Decimal(instance.cart.total) + (Decimal(instance.quantity) * Decimal(instance.product.price))
    instance.cart.count = int(instance.cart.count) + int(instance.quantity)
    instance.cart.updated = datetime.now()
    instance.cart.save()


@receiver(pre_delete, sender=product_models.Entry)
def update_delete_cart(sender, instance, **kwargs):
    instance.cart.total = Decimal(instance.cart.total) - (Decimal(instance.quantity) * Decimal(instance.product.price))
    instance.cart.count -= int(instance.quantity)
    instance.cart.updated = datetime.now()
    instance.cart.save()