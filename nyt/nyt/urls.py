from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Add Django site authentication urls (for login, logout, pwd)
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('api_access.urls')),
    path('admin/', admin.site.urls),
]
