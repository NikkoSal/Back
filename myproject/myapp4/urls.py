from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register, name='register'),
    path('login/', views.login_def, name='login'),
    path('logout/', views.logout_def, name='logout'),
]
