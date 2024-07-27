# blog/urls.py 

from django.urls import path
from .views import PostDetailView, PostList, blog_index, category_search, blog_category, post_like, unlike_post, courses_index
from django.views.generic import ListView, TemplateView
from . import views

urlpatterns = [
   
    #path('', PostList.as_view(), name='post_list'),
    path('blog/', views.blog_index, name='blog_index'),  # url for posts from navbar
    path('search/', views.category_search, name='category_search'),   #search categories
    path("category/<category>/", views.blog_category, name="blog_category"),   #filter categories
    path("post/<int:pk>/", views.blog_detail, name ="blog_detail" ),  #view by pk instead of slug
    path('post/<int:pk>/like/', views.post_like, name='post_like'),     # like post
    path('post/<int:pk>/unlike/', views.unlike_post, name='unlike_post'), #unlike post
    #path('contact/', views.contact_view, name='contact'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),  #detail view by slug  
    path('courses/', views.courses_index, name='courses'),
    path('index/', views.blog_index, name='blog'),
    ]    