from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_password_email, name='send_password_email'),
]
