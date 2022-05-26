from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", home, name='home'),
    path('create', create, name='create'),
    path("<str:pk>", go, name='go'),
]
