# Generated by Django 2.1.7 on 2019-07-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190513_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=24, null=True),
        ),
    ]
