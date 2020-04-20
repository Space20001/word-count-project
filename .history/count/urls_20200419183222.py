
from django.urls import path
from . import

urlpatterns = [
    path('', include(count.urls),
    path('admin/', admin.site.urls),
]
