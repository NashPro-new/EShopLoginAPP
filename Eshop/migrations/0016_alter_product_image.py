# Generated by Django 4.1.7 on 2023-04-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0015_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
