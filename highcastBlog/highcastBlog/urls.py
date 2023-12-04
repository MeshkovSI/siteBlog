from django.contrib import admin
from django.urls import path, include
from .vievs import *

urlpatterns = [
    path('', main_page),
    path('', main_page),
    path('post/', post_page),
    path('about/', about_page),
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
