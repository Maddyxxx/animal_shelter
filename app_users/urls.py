from django.urls import path
from app_users.views import UserLoginView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login')
]