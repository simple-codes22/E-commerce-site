from django.shortcuts import render, redirect
from .models import Store
from datetime import date

def main(request, *args, **kwargs):
    return render(request, 'home.html', {})

def register(request, *args, **kwargs):
    if request.method == "POST":
        form_ = request.POST
        Store.objects.create(
            first_name=form_.get('first-name'),
            last_name=form_.get('last-name'),
            age=form_.get('age'),
            user_name=form_.get('user-name'),
            e_Mail=form_.get('e-mail'),
            Amount=0.00,
            date_registered=date.today(),
            password=form_.get('password')
        )
        temp_redir = Store.objects.get(user_name=form_.get('user-name'), password=form_.get('password'))
        return temp_redir.access_user()
    return render(request, 'signup.html', {})

def login(request, *args, **kwargs):
    return render(request, 'login.html', {})

def dashboard(request, id, user_name, *args, **kwargs):
    return render(request, 'dashboard.html', {'user_content': Store.objects.get(id=id)})

def support(request, id, user_name, *args, **kwargs):
    return


# Create your views here.
