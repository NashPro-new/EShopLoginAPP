# Generated by Django 4.0.5 on 2022-06-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0009_alter_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default=-19800, unique=True),
        ),
    ]