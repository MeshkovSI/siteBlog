from django.urls import path
from .views import *

urlpatterns = [
    path('feedback/', feedback_page),
    path('thanks/', thanks_page, name="thanks_page"),
]