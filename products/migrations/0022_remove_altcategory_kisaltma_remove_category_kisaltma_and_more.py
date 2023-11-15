# Generated by Django 4.0.1 on 2023-11-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_product_stokno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='altcategory',
            name='kisaltma',
        ),
        migrations.RemoveField(
            model_name='category',
            name='kisaltma',
        ),
        migrations.AddField(
            model_name='altcategory',
            name='seodescription',
            field=models.CharField(max_length=160, null=True, verbose_name='Kategori Seo Description Gir'),
        ),
        migrations.AddField(
            model_name='category',
            name='seodescription',
            field=models.CharField(max_length=160, null=True, verbose_name='Kategori Seo Description Gir'),
        ),
        migrations.AddField(
            model_name='markamodel',
            name='seodescription',
            field=models.CharField(max_length=160, null=True, verbose_name='Marka Seo Description Gir'),
        ),
        migrations.AlterField(
            model_name='product',
            name='agirlik',
            field=models.IntegerField(blank=True, verbose_name='Ürün Ağırlık Kg'),
        ),
    ]
