from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=60)
    zip_address = models.CharField(max_length=10)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    type = models.CharField(default="shipping", max_length=20)

    def __str__(self):
        return self.user.username

class Setting(models.Model):
    setting = models.TextField(max_length=150)
    value = models.TextField(max_length=150)

    def __str__(self):
        return self.setting

