from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('countthwaorda/', views.counted, name="counting"),
    path('about/', views.about),
    
]
