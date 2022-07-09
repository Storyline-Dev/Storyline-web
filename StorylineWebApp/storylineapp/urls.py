from django.urls import path
from .views import ClientListView
from . import views

urlpatterns = [
    path('', views.home, name='storyline-home'),
]