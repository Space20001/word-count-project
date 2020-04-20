from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('', views.counted),
    path('', views.about),
    
]
