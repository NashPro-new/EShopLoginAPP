# Generated by Django 4.0.5 on 2022-06-17 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_of_product', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.customer')),
                ('ordered_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eshop.products')),
            ],
        ),
    ]