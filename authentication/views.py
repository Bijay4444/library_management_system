from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.views import obtain_auth_token
from .auth_backend import CustomTokenAuthentication

class AuthView(APIView):
    authentication_classes = [CustomTokenAuthentication]

    def post(self, request, *args, **kwargs):
        # Use the built-in obtain_auth_token view for token generation
        response = obtain_auth_token(request._request)
        return response
