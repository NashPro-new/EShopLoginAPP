# Generated by Django 4.0.5 on 2022-06-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0003_product_alter_order_ordered_item_delete_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
    ]
