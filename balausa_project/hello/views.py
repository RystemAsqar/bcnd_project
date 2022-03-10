from dataclasses import field
from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

 # Import TemplateView

# Add the two views we have been talking about  all this time :)
class TaskList(ListView):
      model = Task
    


class TaskCreate(CreateView):
    model= Task
    fields= '__all__'
    success_url = reverse_lazy('tasks')
 
    
