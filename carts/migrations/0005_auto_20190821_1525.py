# Generated by Django 2.1.7 on 2019-08-21 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20190821_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_item',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart_item',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
