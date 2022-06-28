from django import forms
from .models import Customer
#DataFlair
class Customer_create(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('password','email',)