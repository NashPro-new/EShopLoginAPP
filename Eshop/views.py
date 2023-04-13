import imp
import json
from django.core.serializers import serialize
from multiprocessing import context
from pipes import Template
from passlib.hash import pbkdf2_sha256 as pbk
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,DetailView
from Eshop.models import Customer,Product,Order
from .forms import Customer_create
from django.contrib import messages

class Sign_in(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        cust = Customer.get_customer_by_email(email)
        # isvalid = cust.isExists()
        if cust is not None:
            pass2 = Customer.get_pass_byemail(email)
            # flag = pbk.verify(pass1,pass2)
            flag = check_password(pass1,pass2)
            if flag == True:
                if cust.status == True:
                    request.session['customer'] = cust.email
                    # products = Product.get_all_products()
                    # product_list = list(products)
                    # serialized_products = serialize('json', product_list)
                    # request.session['products'] = serialized_products # store the products in the session
                    
                    return redirect('home', id = cust.id)
                else:
                    return redirect('activate',context) 
            else:
                messages.error(request, 'Password Incorrect.')
                return redirect('/')      
        else:
            messages.error(request, 'User does not exist.')
            return redirect('/')
    
    def sign_out(request):
        request.session.clear()
        return redirect('signin')

def sign_up(request):
    if request.method == "POST":
        
        # username = request.POST.get('email')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('password')
        cust = Customer.get_customer_by_email(email)
        # pass2 = pbk.encrypt(pass1,rounds = 12000, salt_size = 32 )
        if cust is None:
            pass2 = make_password(pass1)
            customer = Customer(
                                first_name=fname,
                                last_name=lname,
                                phone=phone,
                                email=email,
                                password=pass2,
                                status = True)

            customer.register()
            messages.success(request, 'You have been registered')
            return redirect('signin')
        else:
            messages.error(request, 'User Already exist.')
            return redirect('signup')
    
    return render(request, 'signup.html')
    
def HomeView(request, id):
    id = int(id)
    products = Product.get_all_products()
    context = {'products': products, 'id': id}
    try:
        cust = Customer.objects.get(id = id)
    except Customer.DoesNotExist:
        return redirect('signin')
    return render(request, 'home.html', context)

    
class ProductView(DetailView):
    def get(self,request):
        return render(request,'product-page.html')

def edit(request, id):
    id = int(id)
    try:
        cust_objects = Customer.objects.get(id = id)
    except Customer.DoesNotExist:
        return redirect('/')
    cust_form = Customer_create(request.GET or None, instance = cust_objects)
    if cust_form.is_valid():
       cust_form.save()
       return redirect('/')
    return render(request, 'edit.html', {'edit_form':cust_form})

def delete_cust(request, id):

    id = int(id)
    try:
        user_objects = Customer.objects.get(id = id)
    except Customer.DoesNotExist:
        return redirect('signin')
    user_objects.delete()
    return redirect('signin')


class Status_activate(View):
    def get(self,request,id):
        id = int(id)
    
        cust = Customer.objects.get(id = id)

        if cust.status == False:
            cust.status = True
            cust.save()
            
            return render(request,'activate.html',{'cust':cust})

    
    def status_deactivate(request,id):
        id = int(id)
    
        user_objects = Customer.objects.get(id = id)

        if user_objects.status == True:
            user_objects.status = False
            user_objects.save()
            return redirect('signin')
        else: 
            print('Deactivated already')
            return redirect('signin')

    

        

