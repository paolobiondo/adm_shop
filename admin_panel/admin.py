from django.contrib import admin
from admin_panel.models import UserAddress, Setting
from django.contrib.auth.models import User
from product import models as product_model

# Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    search_fields = ['user__username',]


admin.site.register(UserAddress,UserAddressAdmin)
admin.site.register(Setting)