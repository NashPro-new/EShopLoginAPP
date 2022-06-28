

from time import timezone
from django.db import models



class Customer(models.Model):
    # username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=400)
    status = models.BooleanField(default= False)
    
    
    def register(self):
        self.save()
    
    def __str__(self):
        return self.first_name
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
  
        return False
    
    @staticmethod
    def get_pass_byemail(email):
        cust1 = Customer.objects.get(email=email)
        return cust1.password

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

class Product(models.Model):
    title = models.CharField(max_length=50)
    price =  models.IntegerField(default=1)
    description =  models.TextField(blank = True, null = True)
    image  = models.ImageField(upload_to = 'uploads/products/', null = True )

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()


class Order(models.Model):
    ordered_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity_of_product = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100,default = '',blank=True)
    phone = models.CharField(max_length=10)
    date = models.DateField()
    status = models.BooleanField(default= False)

    def placeOrder(self):
        self.save()
    
    def __str__(self):
        return self.ordered_item

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
