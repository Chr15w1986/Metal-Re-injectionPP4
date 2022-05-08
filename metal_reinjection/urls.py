"""metal_reinjection URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls'), name='home-urls'),
    path('posts/', include('posts.urls'), name='posts-urls')
]


handler404 = "metal_reinjection.views.page_not_found_view"
handler500 = "metal_reinjection.views.custom_500_error_view"
