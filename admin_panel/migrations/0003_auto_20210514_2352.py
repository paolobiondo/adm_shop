# Generated by Django 3.2.3 on 2021-05-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.TextField(max_length=150)),
                ('value', models.TextField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
