"""metal_reinjection URL Configuration"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('tracks/', include('tracks.urls')),
    path('posts/', include('posts.urls')),
]

handler404 = "metal_reinjection.views.page_not_found_view"
handler500 = "metal_reinjection.views.custom_500_error_view"
