# Generated by Django 3.2.3 on 2021-05-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210517_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.TextField(blank=True),
        ),
    ]