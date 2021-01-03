from django.urls import path
from . import  views

app_name = 'test'
urlpatterns = [
    path('',views.index, name='test_index'),
    path('products/', views.products, name='products'),
    path('product/<int:id>/', views.product, name='product'),
    path('product/edit/<int:id>/', views.edit, name='edit'),
    path('products/new/', views.new, name='new'),
    path('register/', views.user_register, name='user_register')
]
