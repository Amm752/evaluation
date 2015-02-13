from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
# Palmer said to change location to Location for better naming conventions


def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

