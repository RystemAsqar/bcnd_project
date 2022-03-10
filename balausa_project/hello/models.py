from distutils.command.upload import upload
import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank =True
    )
    fullname_user =models.CharField(max_length = 500)
    year_old = models.IntegerField()
    course =  models.IntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    description = models.TextField(null=True,blank = True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user

    class Meta:
        ordering = ['complete']