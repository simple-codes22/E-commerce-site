from django.shortcuts import render
from .models import Store

def main(request, *args, **kwargs):
    return render(request, 'home.html', {})

def register(request, *args, **kwargs):
    if request.method == "POST":
        return
    return render(request, 'signup.html', {})

def login(request, *args, **kwargs):
    return

def dashboard(request, id, user_name, *args, **kwargs):
    return

def support(request, id, user_name, *args, **kwargs):
    return


# Create your views here.
