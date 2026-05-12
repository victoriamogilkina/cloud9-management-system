from . import views
from django.urls import path

urlpatterns = [
    #path('dashboard/', views.dashboard, name="dashboard"),
    path('clients/', views.clients_list, name="client-list"),
    path('create-client/', views.create_client, name="create-client"),
    path('client/<uuid:pk>/delete/', views.delete_client , name='client-delete'),
    path('clients/<uuid:pk>/time-update/', views.update_client_time, name='client-time-update'),

]