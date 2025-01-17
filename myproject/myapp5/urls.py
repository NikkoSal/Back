from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('<int:user_id>/', views.view, name='view_user'),
    path('add/', views.add, name='add_user'),
    path('<int:user_id>/edit/', views.edit, name='edit_user'),
    path('<int:user_id>/delete/', views.delete, name='delete_user'),
]
