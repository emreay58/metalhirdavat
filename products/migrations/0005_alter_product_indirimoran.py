# Generated by Django 4.2.6 on 2023-10-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_img1_product_img2_product_img3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='indirimoran',
            field=models.IntegerField(blank=True, null=True, verbose_name='İndirim Oranı Yüzde Kaç?'),
        ),
    ]
