from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from .models import User,patient,medical
from django.core.mail.backends import console
from django.forms.fields import CharField

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = medical
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
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
        model = medical
        fields = (  
            'token',
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        )
    



    def create(self, validated_data):
        user = medical.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class RegisterpatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = (  
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'doctores'
        )
    

    def create(self, validated_data):
        user = patient.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            doctores = validated_data['doctores']
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


