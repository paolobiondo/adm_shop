from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username', primary_key=True,related_name='user_info')

    #additional fields
    about = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username

class Setting(models.Model):
    setting = models.TextField(max_length=150)
    value = models.TextField(max_length=150)

    def __str__(self):
        return self.setting

