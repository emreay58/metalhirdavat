# Generated by Django 4.0.1 on 2023-11-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_carouselmodel_description_carouselmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Ürün Başlığı Giriniz'),
        ),
    ]
