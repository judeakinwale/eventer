from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserCreationForm


# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            messages.info(request, f"You are logged in as {username}")
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = NewUserCreationForm
    return render(request, "registration/register.html", {"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You've logged out")
    return redirect("home")


def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    
    form = AuthenticationForm()
    return render(request, "registration/login.html", {"form":form})