# Generated by Django 2.1.7 on 2019-08-21 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20190821_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.DeleteModel(
            name='Cart_Item',
        ),
    ]
