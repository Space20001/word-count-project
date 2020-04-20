from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('counted/', views.counted, name="counted"),
    path('about/', views.about, name=),
    
]
