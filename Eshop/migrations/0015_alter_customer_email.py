# Generated by Django 4.1.7 on 2023-04-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0014_customer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
