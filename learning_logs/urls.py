"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views


app_name = 'learning_logs'  # https://stackoverflow.com/a/50011971/5717580

urlpatterns = [
    # homepage
    path('', views.index, name='index'),  # remember adding the name kw-arg
    # topics
    path('topics/', views.topics, name='topics'),
]