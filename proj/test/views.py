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
    return render(req, 'products.html', {'Products': tmp})

@login_required
def product(req, id):
    tmp = get_object_or_404(Products, id=id)
    return render(req, 'product.html', {'product': tmp, 'page_title': tmp.name})

@permission_required('test.change_product')
def edit(req, id):
    if req.method == 'POST':
        form = ProductForm(req.POST)

        if form.is_valid():
            p = Products.objects.get(id=id)
            p.name = form.cleaned_data['name']
            p.price = form.cleaned_data['price']
            p.save()
            return redirect('test:products')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Products.objects.get(id=id)
        form = ProductForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('test.add_product')
def new(req):
    if req.method == 'POST':
        form = ProductForm(req.POST)

        if form.is_valid():
            a = Products(name=form.cleaned_data['name'], price=form.cleaned_data['price'], owner=req.user)
            a.save()
            return redirect('test:products')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = ProductForm()
        return render(req, 'new.html', {'form': form})