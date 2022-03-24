from django.urls import path, include
from .views import LoginView, RegisterView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('viewset/', include(router.urls)), 
    path('viewset/<int:id>/', include(router.urls)), 
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
] 