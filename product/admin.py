from django.contrib import admin
from product.models import Product,Category,Category_Parents, Cart, EntryCart
from django.utils.datetime_safe import datetime

from product.models import Order,EntryOrder


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name',]

class EntryCartAdmin(admin.ModelAdmin):
    # Overide of the save model
    def save_model(self, request, obj, form, change):
        print('test')
        obj.cart.total += obj.quantity * obj.product.price
        obj.cart.count += obj.quantity
        obj.cart.updated = datetime.now()
        obj.cart.save()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.cart.total -= obj.quantity * obj.product.price
        obj.cart.count -= obj.quantity
        obj.cart.updated = datetime.now()
        obj.cart.save()
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.cart.total -= obj.quantity * obj.product.price
            obj.cart.count -= obj.quantity
            obj.cart.updated = datetime.now()
            obj.cart.save()
            super().delete_model(request, obj)
        queryset.delete()


admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Category_Parents)
admin.site.register(Cart)
admin.site.register(EntryCart, EntryCartAdmin)

admin.site.register(Order)
admin.site.register(EntryOrder)