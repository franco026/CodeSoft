from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views

# Views
from .views import current_user, Usersignup

#router = DefaultRouter()
#router.register('users', UserViewSet, basename='users')

urlpatterns = [
    #path('', include(router.urls)),
    path('current_user/', current_user.as_view()),
    path('users/', Usersignup.as_view())

]