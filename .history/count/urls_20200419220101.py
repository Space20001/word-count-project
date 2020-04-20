from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hom'),
    path('counted/', views.counted, name="counting"),
    path('about/', views.about),
    
]
