from django.urls import path
from . import views

# localhost:8000/kapil
urlpatterns = [
    path('', views.all_chai, name='all_kapil'),
]