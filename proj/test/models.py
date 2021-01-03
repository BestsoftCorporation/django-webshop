from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return self.price

    def is_popular(self):
        return self.num_views > 5