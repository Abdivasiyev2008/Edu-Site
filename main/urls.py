from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('video/', post, name='post'),
    path('video/<int:pk>/', VideoDarsDetailView.as_view(), name='video'),
    path('playlist-vid/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
]