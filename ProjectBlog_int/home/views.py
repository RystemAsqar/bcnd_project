from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from home.models import BlogModel
from .forms import BlogForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
    model = BlogModel
    template_name = 'home.html'

def details(request, blog_id):
    model = BlogModel.objects.filter(id=blog_id)
    return render(request,'blog_detail.html', {'object_list': model})

class AddBlogView(CreateView):
    model = BlogModel
    form_class = BlogForm
    template_name = 'add_blog.html'
    # fields = '__all__'   

    # fields = ('title', 'title_tag', 'user', 'content') 

class UpdatePostView(UpdateView): 
    model = BlogModel
    template_name = 'update_blog.html'
    fields = ['title', 'title_tag', 'image', 'content']

class DeleteViewPost(DeleteView): 
    model = BlogModel
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')