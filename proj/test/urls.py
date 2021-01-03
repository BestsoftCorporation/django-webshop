from django.urls import path
from . import  views

app_name = 'test'
urlpatterns = [
    path('',views.index, name='test_index'),
    path('products/', views.products, name='products'),
    path('products/new/', views.new, name='new')
]
