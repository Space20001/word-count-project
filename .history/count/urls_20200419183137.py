
from django.urls import path, include

urlpatterns = [
    path('', include(count.urls),
    path('admin/', admin.site.urls),
]
