from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from blog.views import home_view

urlpatterns = [
    
    path('', home_view.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls')),    
    path('', home_view.as_view(), name='home'),
    ]
