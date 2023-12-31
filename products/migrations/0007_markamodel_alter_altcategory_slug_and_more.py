# Generated by Django 4.0.1 on 2023-10-22 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_marka_alter_product_altcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Marka Oluşturunuz')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='altcategory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='indirimoran',
            field=models.IntegerField(blank=True, verbose_name='İndirim Oranı Yüzde Kaç?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='marka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.markamodel', verbose_name='Ürün Markası Girin'),
        ),
    ]
