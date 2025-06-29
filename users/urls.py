from django.urls import path
from users import RegisterView,LoginView

urlpatterns = [
    path('/auth/register/',RegisterView.as_view()),
    path('/auth/login/',LoginView.as_view()),
]