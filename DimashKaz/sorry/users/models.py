from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)   
    phone =models.CharField(max_length=100) 
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)




      