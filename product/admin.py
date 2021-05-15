from django.contrib import admin
from product.models import Product,Category,Category_Parents

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name',]

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Category_Parents)