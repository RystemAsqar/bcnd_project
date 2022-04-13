from unicodedata import name
from django.urls import path
# from . import views
from .views import HomeView,DeleteViewPost,ArticleDetailView

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('article/<int:pk>/remove', DeleteViewPost.as_view(), name = "delete_post"),
]
