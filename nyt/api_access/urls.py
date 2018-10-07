from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signout/', views.signout, name='signout'),  # remember the trailing /
    path('profile/', views.profile, name='profile'),
]
