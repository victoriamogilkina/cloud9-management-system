from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('clients/', views.clients_list, name="client_list"),
    path('create_client/', views.create_client, name="create_client")

]