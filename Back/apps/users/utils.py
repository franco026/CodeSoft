from .serializers import UsersSerializer


def custom_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UsersSerializer(user, context={'request': request}).data,
    }