from distutils.command.upload import upload
import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
   
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank =True)
    fullname_user =models.CharField(('Name and Surname'),max_length = 500)
    year_old = models.IntegerField('Age')
    course =  models.IntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    my_choices=(
    ('1' , 'Yes, I can'),
    ('2' , 'No, I can not'),
    ('3', 'I want to learn to play'),
    )
    choice = models.CharField(('Can you play dombyra'),max_length=30,blank=True,null=True,choices=my_choices)
    description = models.TextField(('Your other skills and some facts'),null=True,blank = True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user

    class Meta:
        ordering = ['complete']


class Task_music(models.Model):
       
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank =True)
    fullname_user =models.CharField(('Name and Surname'),max_length = 500)
    year_old = models.IntegerField('Age')
    course =  models.IntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    my_choices=(
    ('1' , 'Yes, I can'),
    ('2' , 'No, I can not'),
    ('3', ' I can play instruments'),
    )
    choice = models.CharField(('Can you sing songs ? '),max_length=30,blank=True,null=True,choices=my_choices)
    description = models.TextField(('Your other skills and some facts'),null=True,blank = True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user        