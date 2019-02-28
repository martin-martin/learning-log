"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views


urlpatterns = [
    # homepage
    path('', views.index, name='index'),
]