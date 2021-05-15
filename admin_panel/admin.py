from django.contrib import admin
from admin_panel.models import UserProfileInfo, Setting

# Register your models here.
class UserProfileInfoAdmin(admin.ModelAdmin):
    search_fields = ['user__username',]

admin.site.register(UserProfileInfo,UserProfileInfoAdmin)
admin.site.register(Setting)