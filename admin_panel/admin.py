from django.contrib import admin
from admin_panel.models import UserAddress, Setting
from django.contrib.auth.models import User
from product import models as product_model

class UserAdmin(admin.ModelAdmin):
    # list_display = ('email', 'first_name', 'last_name')
    # list_filter = ('is_staff', 'is_superuser')
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        product_model.Cart.objects.create(user=obj)

# Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    search_fields = ['user__username',]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserAddress,UserAddressAdmin)
admin.site.register(Setting)