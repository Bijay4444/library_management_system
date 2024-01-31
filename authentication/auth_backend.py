
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

# Custom token authentication class for token authentication
class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        try:
            auth_type, token = auth_header.split()
        except ValueError:
            return None

        if auth_type.lower() != 'token':
            return None

        return self.authenticate_credentials(token)
