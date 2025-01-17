from django.urls import path
from . import views

urlpatterns = [
    path('end/', views.endpoint, name='endpoint'),
    path('redir/', views.redirected, name='redirected'),
]

