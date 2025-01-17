from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.post1, name='post1'),
    path('sum/', views.post2, name='post2'),
    path('sh/', views.get, name='get'),
]

