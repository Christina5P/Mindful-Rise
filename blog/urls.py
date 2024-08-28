# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view.as_view(), name='home'),  # Home page view
    path('blog/', views.blog_index, name='blog_index'),  # Main blog index page
    path(
        'index/', views.blog_index, name='blog'
    ),  # Alternate route to blog index (consider removing if redundant)
    path(
        'post/<slug:slug>/', views.blog_detail, name='post_detail'
    ),  # Blog detail view by slug
    path(
        'category/<slug:category_slug>/',
        views.blog_category,
        name='blog_category',
    ),  # Filtered view by category
    path(
        'search/', views.category_search, name='category_search'
    ),  # Category search functionality
    path(
        'like_post/<int:post_id>/', views.like_post, name='like_post'
    ),  # Like/unlike post AJAX view
    path(
        'post/<slug:slug>/edit_comment/<int:comment_id>/',
        views.comment_edit,
        name='comment_edit',
    ),  # Edit comment
    path(
        'post/<slug:slug>/comment_delete/<int:comment_id>/',
        views.comment_delete,
        name='comment_delete',
    ),  # Delete comment
    path('courses/', views.courses_view, name='courses'),  # List of courses
    path(
        'course/<slug:slug>/', views.course_detail, name='course_detail'
    ),  # Course detail view
    path(
        '<path:resource>',
        views.TemplateView.as_view(template_name='404.html'),
        name='404',
    ),  # Catch-all 404 view
    # User authentication paths
    path('login/', views.login_view, name='login'),  # User login view
    path('signup/', views.signup_view, name='signup'),  # User signup view

    
]
