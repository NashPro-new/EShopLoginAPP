from django.contrib import admin
from Eshop.models import Customer,Order,Product

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)