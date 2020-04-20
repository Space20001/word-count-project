from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('counted/', views.counted, ),
    path('about/', views.about),
    
]
