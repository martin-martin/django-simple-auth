from django.urls import path
from . import views


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signout/', views.signout, name='signout'),  # remember the trailing /
    path('profile/', views.profile, name='profile'),
]
