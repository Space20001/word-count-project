
from django.urls import path
from . import views

urlpatterns = [
    path('', t.urls'),
    path('admin/', admin.site.urls),
]
