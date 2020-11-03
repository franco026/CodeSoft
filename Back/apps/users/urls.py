from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views

# Views
from .views import current_user, Usersignup, Usersignuppatient, Usersignupdoctor

router = DefaultRouter()
router.register('patient', Usersignuppatient, basename='patient')
router.register('doctor', Usersignupdoctor, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
    path('current/', current_user.as_view()),
    path('users/', Usersignup.as_view()),

]