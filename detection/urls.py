# detection/urls.py
from django.urls import path
from .views import index, video_feed

urlpatterns = [
    path('', index, name='home'),
    path('video_feed/', video_feed, name='video_feed'),
]






