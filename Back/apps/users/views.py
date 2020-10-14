from django.shortcuts import render
from rest_framework import viewsets,generics

from .models import User
from .serializers import UsersSerializer
# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class = UsersSerializer

class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer    