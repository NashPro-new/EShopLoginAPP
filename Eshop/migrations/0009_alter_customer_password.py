# Generated by Django 4.0.5 on 2022-06-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0008_customer_slug_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=400),
        ),
    ]
