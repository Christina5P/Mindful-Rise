# blog/urls.py 

from . import views
from django.urls import path
from.views import Post, Comment, Category, Courses, blog_index
from django.views.generic import ListView, TemplateView


urlpatterns = [
   
    #path('carousel/', views.carousel, name='carousel'),
    path('', views.PostList.as_view(), name='post_list'),
    path('blog/', views.blog_index, name='blog_index'),
    path('search/', views.category_search, name='category_search'),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("post/<int:pk>/", views.blog_detail, name ="blog_detail" ),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    #path('contact/', views.contact_view, name='contact'),
    #path('<slug:slug>/', views.post, name='post'),
    path('courses/', views.courses_index, name='courses'),
    path('index/', views.blog_index, name='blog'),

    ]    