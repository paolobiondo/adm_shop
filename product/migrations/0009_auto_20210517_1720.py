# Generated by Django 3.2.3 on 2021-05-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_cart_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.TextField(blank=True),
        ),
    ]
