from dataclasses import field
from django.forms import DateInput, widgets
from django.test import client
from users.forms import ClientRegisterForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Client

class DateInput(DateInput):
    input_type = 'date'

def home(request):
    return render(request, 'storylineapp/home.html')

class ClientListView(ListView):
    model = Client
    template_name = 'users/clinicianHome.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Client.objects.filter(therapist=user).order_by('-firstName')

class ClientDetailView(DetailView):
    model = Client

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'storylineapp/add_client_form.html'
    form_class = ClientRegisterForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    template_name = 'storylineapp/client_update_form.html'
    form_class = ClientRegisterForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        client = self.get_object()
        if self.request.user == client.therapist:
            return True
        return False

class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = '/'

    def test_func(self):
        client = self.get_object()
        if self.request.user == client.therapist:
            return True
        return False