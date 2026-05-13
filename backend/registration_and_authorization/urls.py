from . import views
from django.urls import path

urlpatterns = [
    path('', views.start, name="start"),
    path('registration/', views.register, name="registration"),
    path('log-in/', views.log_in, name="log-in"),
    path('log-out/', views.log_out, name="log-out")
]