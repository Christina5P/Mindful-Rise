from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    # path('', home_view.as_view(), name='home'),
    path('', include('blog.urls')),
]
