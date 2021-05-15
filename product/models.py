from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.FloatField(null=True, blank=True)
    discount_price = models.FloatField(null=True, blank=True)
    units = models.IntegerField()
    cover = models.ImageField(upload_to='covers/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)    

    def __str__(self):
        return self.name

class Category_Parents(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='id', related_name='parent')
    child = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='id', related_name='child')

    def __str__(self):
        return str(self.parent)+' -> '+str(self.child)