from django.urls import include, path
from rest_framework import routers
from audiofile_api import views

app_label = 'audiofile'

urlpatterns = [
    path('song/',views.SongList.as_view(),name="details"),
    path('song/<int:pk>/',views.SongList.as_view(),name="details"),
    path('podcast/',views.PodcastList.as_view(),name="details"),
    path('podcast/<int:pk>/',views.PodcastList.as_view(),name="details"),
    path('audiobook/',views.AudiobookList.as_view(),name="details"),
    path('audiobook/<int:pk>/',views.AudiobookList.as_view(),name="details"),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]