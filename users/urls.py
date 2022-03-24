from django.urls import path, include
from .views import profile, dashboard, signup, signin, logout, change_password

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
]