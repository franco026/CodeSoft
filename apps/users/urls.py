from django.urls import path

from apps.users.views import Login, CreateUser, account


urlpatterns = [
    path('', Login, name = 'login'),
    path('signup/', CreateUser , name='signup'),
    path('account/', account , name='account'),
]