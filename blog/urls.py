# blog/urls.py 

from django.urls import path, include
from .views import PostDetailView, PostList, blog_index, category_search, blog_category, like_post, courses_index
from django.views.generic import DetailView, ListView, TemplateView
from . import views


urlpatterns = [
 
    #path('', PostList.as_view(), name='home'),
    path('blog/', views.blog_index, name='blog_index'),  # url for posts from navbar
    path('post/<slug:slug>/', views.blog_detail, name='post_detail'),  #detail view by slug  
    path("category/<category>/", views.blog_category, name="blog_category"),   #filter categories
    path('like/<int:post_id>/', like_post, name='like_post'),  # like/unlike post
    path('post/<slug:slug>/edit_comment/<int:comment_id>',
       views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>',
       views.comment_delete, name='comment_delete'),
    path('courses/', views.courses_index, name='courses'),
    path('index/', views.blog_index, name='blog'),
    path('search/', views.category_search, name='category_search'),   #search categories
    path('accounts/', include('allauth.urls')),
    path('valuation/signup/', views.signup_view, name='signup'),
    ]    