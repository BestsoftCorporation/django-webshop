from .models import Products
from django.forms import ModelForm, Form
import django.forms as f

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'content']