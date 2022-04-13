from audioop import reverse
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView
from .models import Post
from django.urls import reverse_lazy

def home(request): 
    return render(request, 'home.html', {})

class HomeView(ListView): 
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView): 
    model = Post
    template_name = 'article_details.html'


class DeleteViewPost(DeleteView): 
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')