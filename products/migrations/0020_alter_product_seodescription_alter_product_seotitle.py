# Generated by Django 4.0.1 on 2023-11-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_seodescription_alter_product_seotitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seodescription',
            field=models.TextField(max_length=160, null=True, verbose_name='Seo Açıklama Giriniz'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seotitle',
            field=models.CharField(max_length=60, null=True, verbose_name='Seo Başlığı Giriniz'),
        ),
    ]
