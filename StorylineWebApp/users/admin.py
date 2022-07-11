from django.contrib import admin
from .models import Profile
from storylineapp.models import Client

admin.site.register(Profile)
admin.site.register(Client)
