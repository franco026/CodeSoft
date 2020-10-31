from .models import User
from django.http import HttpResponseRedirect
from rest_framework import permissions, status,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsersSerializer, RegisterSerializer


class current_user(APIView):
    """
    Determine the current user by their token, and return their data
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)


#class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

#    permission_classes = (permissions.AllowAny,)
#
#    def post(self, request, format=None):
#        serializer = UserSerializerWithToken(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Usersignup(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data =  RegisterSerializer(user).data
        return Response({"response" : "success", "message" : "user created succesfully"})
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
