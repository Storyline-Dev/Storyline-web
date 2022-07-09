from django.shortcuts import render
from django.views.generic import ListView
from .models import Client

clients = [
    {
        'name': 'Elsie Reed',
        'dob': '10-14-1989',
        'email':'elsie.reed@gmail.com',
        'gender':'Female',
        'race':'white',
        'profession':'student',
        'start_date':'01-20-2021',
        'last_session':'03-02-2022',
        'session_count':'19',
        'activity_status':'true',
        'therapist':'Wally Walleye'
    },
    {
        'name': 'Rebecca Watters',
        'dob': '05-15-1997',
        'email':'beccawatts@gmail.com',
        'gender':'Female',
        'race':'white',
        'profession':'nurse',
        'start_date':'01-20-2021',
        'last_session':'05-02-2022',
        'session_count':'25',
        'activity_status':'true',
        'therapist':'Wally Walleye'
    }
]

def home(request):
    context = {
        'clients': clients
    }
    return render(request, 'users/clinicianHome.html', context)

class ClientListView(ListView):
    model = Client
    template_name = 'storyline/home.html'