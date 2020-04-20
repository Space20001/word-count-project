
from django.urls import path
from . import views

urlpatterns = [
    path('', views.urls'),
    path('admin/', admin.site.urls),
]
