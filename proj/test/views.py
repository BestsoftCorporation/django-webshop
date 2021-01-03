from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Products
from .forms import ProductForm

def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})
    else:
        return redirect('test:products')

login_required
def products(req):
    tmp = Products.objects.all()
    return render(req, 'products.html', {'articles': tmp})

@permission_required('test.add_product')
def new(req):
    if req.method == 'POST':
        form = ProductForm(req.POST)

        if form.is_valid():
            a = Products(title=form.cleaned_data['title'], content=form.cleaned_data['content'], owner=req.user)
            a.save()
            return redirect('test:products')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = ProductForm()
        return render(req, 'new.html', {'form': form})