from django.contrib import admin
from admin_panel.models import UserProfileInfo

# Register your models here.
class UserProfileInfoAdmin(admin.ModelAdmin):
    search_fields = ['user__username',]

admin.site.register(UserProfileInfo,UserProfileInfoAdmin)