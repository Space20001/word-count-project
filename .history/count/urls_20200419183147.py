
from django.urls import path


urlpatterns = [
    path('', include(count.urls),
    path('admin/', admin.site.urls),
]
