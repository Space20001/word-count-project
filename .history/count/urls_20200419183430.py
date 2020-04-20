
from django.urls import path
from . import views

urlpatterns = [
    path('', include('count.urls'),
    path('admin/', admin.site.urls),
]
