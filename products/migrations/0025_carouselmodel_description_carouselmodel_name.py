# Generated by Django 4.0.1 on 2023-11-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_carouselmodel_alter_altcategory_seodescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselmodel',
            name='description',
            field=models.TextField(null=True, verbose_name='Açıklama Girin'),
        ),
        migrations.AddField(
            model_name='carouselmodel',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Caroseul Açıklama Gir'),
        ),
    ]
