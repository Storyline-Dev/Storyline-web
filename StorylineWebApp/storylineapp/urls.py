from django.urls import path
from .views import (
    ClientListView, 
    ClientDetailView, 
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='storyline-home'),
    path('user/<str:username>/', ClientListView.as_view(), name='clinician-home'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]