from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .models import Products, Review
from .forms import ProductForm, RegisterForm, ReviewForm


def index(req):
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})


@permission_required('test.change_product')
@login_required
def panel(req):
    tmp = Products.objects.all()
    return render(req, 'admin.html', {'Products': tmp})

#@login_required
def products(req):
    tmp = Products.objects.all()
    return render(req, 'products.html', {'Products': tmp})


def product(req, id):
    tmp = get_object_or_404(Products, id=id)
    rev = Review.objects.filter(product=tmp)
    return render(req, 'product.html', {'product': tmp, 'page_title': tmp.name,'rev':rev})

@permission_required('test.change_product')
def edit(req, id):
    if req.method == 'POST':
        form = ProductForm(req.POST, req.FILES)

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

@permission_required('test.change_product')
@login_required
def delete(req, id):
    Products.objects.filter(id=id).delete()
    tmp = Products.objects.all()
    return render(req, 'admin.html', {'Products': tmp})



@permission_required('test.add_product')
def new(req):
    if req.method == 'POST':
        form = ProductForm(req.POST, req.FILES)

        if form.is_valid():

            a = Products(name=form.cleaned_data['name'], price=form.cleaned_data['price'], image=req.FILES['image'], owner=req.user)
            a.save()
            return redirect('test:products')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = ProductForm()
        return render(req, 'new.html', {'form': form})

@login_required()
def review(req,id):
    if req.method == 'POST':
        form = ReviewForm(req.POST)

        if form.is_valid():

            r = Review(comment=form.cleaned_data['comment'], product=Products.objects.get(id=id),owner=req.user)
            r.save()
            return redirect('/product/'+str(id))
        else:
            #return redirect('/product/' + str(id))
            tmp = get_object_or_404(Products, id=id)
            return render(req, 'product.html', {'product': tmp, 'page_title': tmp.name,'form': form})
    else:
        return redirect('/product/'+str(id))

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})