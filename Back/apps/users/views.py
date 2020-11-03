from .models import User, patient, medical
from django.http import HttpResponseRedirect
from rest_framework import permissions, status,views, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsersSerializer, RegisterSerializer, RegisterpatientSerializer


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
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data =  RegisterSerializer(user).data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)

class Usersignuppatient(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = patient.objects.all()
    serializer_class = RegisterpatientSerializer
    def post(self, request):
        print(request.data)
        serializer = RegisterpatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data =  RegisterpatientSerializer(user).data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)


class Usersignupdoctor(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = medical.objects.all()
    serializer_class = RegisterSerializer
    def post(self, request):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data =  RegisterSerializer(user).data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
        
         
    
    
