from django.contrib import admin

# Register your models here.
from .models import Products,Review

admin.site.register(Products)
admin.site.register(Review)