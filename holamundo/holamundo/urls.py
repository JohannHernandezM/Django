from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('miembros/', include('miembros.urls')),
    path('admin/', admin.site.urls)
]