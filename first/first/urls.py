from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('secondapp/',include('secondapp.urls',namespace='secondapp')),
]
