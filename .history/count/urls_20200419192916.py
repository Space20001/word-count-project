from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('countth waorda/', views.counted, name="counting"),
    path('about/', views.about),
    
]
