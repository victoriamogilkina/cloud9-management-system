from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import MyUserCreationForm, MyLoginForm

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = MyUserCreationForm()

    return render(request, "accounts/registration.html", {"form": form})

def log_in(request):
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = MyLoginForm()

    return render(request, "accounts/login.html", {"form": form})

def log_out(request):
    logout(request)
    return redirect("log-in")