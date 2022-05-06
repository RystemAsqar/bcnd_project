from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    title_tag = models.CharField(max_length=1000, default="SDU BLOG")
    content = models.TextField()
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')    