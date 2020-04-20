from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('counted/', views.counted, name=""),
    path('about/', views.about),
    
]
