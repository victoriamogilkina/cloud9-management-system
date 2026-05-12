from django.shortcuts import render, redirect
from .models import Clients
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from .forms import PostClient

# Create your views here.
@login_required
def clients_list(request):
    clients_data = Clients.objects.all()
    return render(request, "", clients_data)


@role_required('admin')
def create_client(request):
    if request.method == "POST":
        form = PostClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
        return PostClient()
    return render(request, "clients/Create_Client.html", {"form" : form})



