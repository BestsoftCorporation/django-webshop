from .models import Products
from django.forms import ModelForm, Form
import django.forms as f

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'image']

class RegisterForm(f.Form):
    username = f.CharField(widget=f.TextInput(attrs={'class':'form-control'}))
    email = f.EmailField(widget=f.EmailInput(attrs={'class':'form-control'}))
    password = f.CharField(widget=f.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = f.CharField(widget=f.PasswordInput(attrs={'class':'form-control'}))
    first_name = f.CharField(widget=f.TextInput(attrs={'class':'form-control'}))
    last_name = f.CharField(widget=f.TextInput(attrs={'class':'form-control'}))
    phone_number = f.CharField(widget=f.NumberInput(attrs={'class':'form-control'}), required=False)
