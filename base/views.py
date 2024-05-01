from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from pyexpat.errors import *
from django.contrib import messages
from .forms import NewUserForm
from .models import Data
from django.http import HttpResponseRedirect


@login_required(login_url='login')
def base(request):
    return render(request, 'base/base.html')


@login_required(login_url='login')
def about(request):
    return render(request, 'base/about.html')


@login_required(login_url='login')
def links(request):
    return render(request, 'base/links.html')


@login_required(login_url='login')
def bot(request):
    return render(request, 'base/bot.html')


@login_required(login_url='login')
def database(request):
    data = Data.objects.order_by('-datetime')
    return render(request, 'base/database_main.html', {'data': data})


def login(request):
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def registration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        messages.error(request, "Registration failed")
    form = NewUserForm()
    return render(request=request, template_name="registration/registration.html", context={"register_form": form})
