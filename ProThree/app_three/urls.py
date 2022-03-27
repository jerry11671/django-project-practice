from django.urls import path
from .views import index, Users

urlpatterns = [
    path('', index, name='index'),
    path('user/', Users, name='user'),
]
