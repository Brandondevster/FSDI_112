
from django.contrib import admin
from django.urls import path, include
from .views import HOME, ABOUT

urlpatterns = [
    path('', HOME.as_view(), name="home"),
    path('about/', ABOUT.as_view(), name="about"),
]