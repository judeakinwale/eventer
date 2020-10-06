# Generated by Django 2.1.7 on 2019-08-21 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20190821_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='carts.Cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_total',
            field=models.DecimalField(decimal_places=2, default=1000.99, max_digits=1000),
        ),
    ]