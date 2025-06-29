from django.urls import path
from .views import firebase_login,firebase_register

urlpatterns = [
    path('auth/register/',firebase_register, name='firebase_register'),
    path('auth/login/',firebase_login,name='firebase_login'),
]