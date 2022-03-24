from dataclasses import field
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task,Task_music
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

 # Import TemplateView

# Add the two views we have been talking about  all this time :)
def Task_list(request):
      template = "task_list.html"
      context = {}
      return render(request,template,context)

class TaskList(ListView):
      model = Task
    


class TaskCreate(CreateView):
    model= Task
    fields= '__all__'
    success_url = reverse_lazy('tasks')


def Task_list_music(request):
      template = "task_list.html"
      context = {}
      return render(request,template,context)

class Taskmusic(ListView):
      model = Task
 
class TaskCreateMusic(CreateView):
    model= Task_music
    fields= '__all__'
    success_url = reverse_lazy('taskmusic')
    
