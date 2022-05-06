from django.urls import path
from .views import HomeView, AddBlogView, UpdatePostView, DeleteViewPost
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.home, name="home"),

    path('', HomeView.as_view(), name="home"),
    path('blog/<int:blog_id>', views.details, name='blog_detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('blog/<int:pk>/remove', DeleteViewPost.as_view(), name = "delete_post"),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)