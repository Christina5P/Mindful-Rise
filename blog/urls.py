# blog/urls.py 


from django.urls import path, include
from .views import DetailView, blog_index, category_search, blog_category, like_post, courses_view, home_view, login_view, signup_view
from django.views.generic import DetailView, ListView, TemplateView
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
 
   path('blog/', views.blog_index, name='blog_index'),  # url for posts from navbar
   path('index/', views.blog_index, name='blog'), # view to blog index
   path('post/<slug:slug>/', views.blog_detail, name='post_detail'),  # detail view by slug  
   path('category/<slug:category_slug>/', views.blog_category, name='blog_category'),
   path('search/', views.category_search, name='category_search'),
   path('like_post/<int:post_id>/', like_post, name='like_post'),
   path('post/<slug:slug>/edit_comment/<int:comment_id>',
      views.comment_edit, name='comment_edit'),
   path('post/<slug:slug>/delete_comment/<int:comment_id>',
      views.comment_delete, name='comment_delete'),
   path('courses/', views.courses_view, name='courses'), # url to course index
   path('course/<slug:slug>/', views.course_detail, name='course_detail'), # open a course card
   path('accounts/', include('allauth.urls')),  # Djangos path incl to register and login
   path('', home_view.as_view(), name='home'), 
   path('login/', login_view, name='login'),  # Login URL
   path('signup/', signup_view, name='signup'),  # Signup URL
    ]    

