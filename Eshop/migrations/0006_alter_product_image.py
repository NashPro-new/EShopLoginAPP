# Generated by Django 4.0.5 on 2022-06-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0005_rename_product_name_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
