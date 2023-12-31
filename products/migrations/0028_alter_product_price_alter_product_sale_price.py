# Generated by Django 4.0.1 on 2023-11-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_customer_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Ürün Fiyatı'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Ürün İndirimli Fiyatı'),
        ),
    ]
