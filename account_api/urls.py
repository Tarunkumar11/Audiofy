from django.urls import include, path
from rest_framework import routers
from account_api import views

app_label = 'account'
#router = routers.DefaultRouter()
#router.register(r'SongList', views.SongList)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('users/', views.UserCreate.as_view()),
    path('users/<int:pk>/', views.UserCreate.as_view())
]