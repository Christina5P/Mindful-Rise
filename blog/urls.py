# blog/urls.py 

from django.urls import path, include
from .views import PostDetailView, PostList, blog_index, category_search, blog_category, like_post, courses_index, home_view, login_view, signup_view
from django.views.generic import DetailView, ListView, TemplateView
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
 
    #path('', PostList.as_view(), name='home'),
   path('blog/', views.blog_index, name='blog_index'),  # url for posts from navbar
   path('post/<slug:slug>/', views.blog_detail, name='post_detail'),  #detail view by slug  
   path("category/<str:category>/", views.blog_category, name="blog_category"),
   path('search/', views.category_search, name='category_search'),
   path('like-post/<int:post_id>/', like_post, name='like_post'), # like/unlike post
   path('post/<slug:slug>/edit_comment/<int:comment_id>',
      views.comment_edit, name='comment_edit'),
   path('post/<slug:slug>/delete_comment/<int:comment_id>',
      views.comment_delete, name='comment_delete'),
   path('courses/', views.courses_index, name='courses'),
   path('index/', views.blog_index, name='blog'),
   path('accounts/', include('allauth.urls')),
   path('', home_view.as_view(), name='home'), 
   #path('category/<str:category>/', CatListView.as_view(), name='category'),
   #path('login/', login_view, name='login'),  # Login URL
   #path('signup/', signup_view, name='signup'),  # Signup URL
    ]    

