from django.contrib import admin
from product.models import Product,Category,Category_Parents, Cart, EntryCart
from django.utils.datetime_safe import datetime

from product.models import Order,EntryOrder


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name',]

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Category_Parents)
admin.site.register(Cart)
admin.site.register(EntryCart)

admin.site.register(Order)
admin.site.register(EntryOrder)