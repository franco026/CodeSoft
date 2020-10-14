from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id'
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'document_type',
            'document_number'
            'is_medical',
            'is_patient',
            'is_connected'
        )

        extra_kwargs = {
            'document_number': {"write_only": True, 'required': True}
            }
    
    def create(self, validated_data):
        profile_data= validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        user.save()

        return user 
