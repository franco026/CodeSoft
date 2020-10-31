from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from .models import User,patient
from django.core.mail.backends import console
from django.forms.fields import CharField

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_type',
            'first_name',
            'last_name',
            'email',
            'is_connected',
        )

class RegisterSerializer(serializers.ModelSerializer):
    password_confirmation =  serializers.CharField(max_length=64)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message='Lo sentimos, alguien ya ha sido fichado con este correo electrónico')])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message='Lo sentimos, alguien ya ha sido fichado con este correo electrónico')])
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
    
    class Meta:
        
        
        model = User
        fields = (  
            'token',
            'username',
            'email',
            'password',
            'password_confirmation',
            'first_name',
            'last_name',
        )
    
    def validate(self, data):
        passwd = data.get('password')
        passwd_conf = data.get('password_confirmation')
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
       
        return data 


    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



    
    #def create(self, validated_data):
    #    profile_data= validated_data.pop('profile')
    #    user = User.objects.create_user(**validated_data)
    #    user.save()

    #    return user 

#    def llamar(self, validated_data):
#        patient = validated_data.get('is_patient')
#        if patient:
#            patientyes = PatientSerializer(many = True)
#        else:
#            return validated_data


