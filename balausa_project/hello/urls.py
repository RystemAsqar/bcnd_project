
from unicodedata import name
from django.urls import path
from .views import TaskList,TaskCreate,Taskmusic,Task_list,TaskCreateMusic

urlpatterns = [
    path('',TaskList.as_view(),name = 'tasks'),
    path('',Taskmusic.as_view(),name = 'taskmusic'),
    path('task-create/' , TaskCreate.as_view(),name='task-create'),
    path('', Task_list, name='Home'),
    path('task-music/',TaskCreateMusic.as_view(),name='task-music'),
]
