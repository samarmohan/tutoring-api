from django.urls import path, include

from knox.views import LogoutView

from .api import UserAPI, RegisterAPI, LoginAPI

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPI.as_view()),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout')
]
