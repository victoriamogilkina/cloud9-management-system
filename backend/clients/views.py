from django.shortcuts import get_object_or_404, render, redirect
from .models import Clients
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from .forms import PostClient, AddTime
from django.utils import timezone
from django.db.models import Q


# Create your views here.
@login_required
def clients_list(request):
    query = request.GET.get('q', '')
    qs = Clients.objects.all()
    if query:
        qs = qs.filter(
            Q(full_name__icontains=query) |
            Q(pc_number__icontains=query)
        )
    now = timezone.now().date()
    active_clients = qs.filter(expires_at__date__gte=now).order_by('-expires_at')
    expired_clients = qs.filter(expires_at__date__lt=now).order_by('expires_at')
    
    context = {
        'active_clients': active_clients,
        'expired_clients': expired_clients,
        'query': query,  
    }
    return render(request, 'clients/Client_list.html', context)


@login_required
def dashboard(request):
    aware_dt = timezone.now()
    active_clients = Clients.objects.exclude(expires_at__lt=aware_dt)
    my_pc = 25
    for i in active_clients:
        my_pc - 1
    
    return render(
        request,
        "clients/dashboard.html",
        {"active_clients": active_clients, "my_pc": my_pc},
    )

@role_required("admin")
def create_client(request):
    if request.method == "POST":
        form = PostClient(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect("client-list")
    form = PostClient()
    return render(request, "clients/Create_Client.html", {"form": form})


@role_required("admin")
def delete_client(request, pk):
    client = get_object_or_404(Clients, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect("client-list")
    return render(request, "clients/client_confirm_delete.html", {"client": client})


@role_required("admin")
def update_client_time(request, pk):
    client = get_object_or_404(Clients, pk=pk)
    if request.method == "POST":
        form = AddTime(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client-list")
    form = AddTime()
    return render(request, "clients/add_time.html", {"form": form})
