from django.contrib import admin
from django.urls import path, include

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
]
