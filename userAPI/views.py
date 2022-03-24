from django.contrib.auth import authenticate
import jwt
from .models import jwt
from .models import CustomUser
from datetime import datetime, timedelta
from django.conf import settings
import random
import string
from rest_framework.views import APIView
from .serializer import LoginSerializer, RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
#___________________________________________________________________________________________________________________________________________________________

#___________________________________________________________________________________________________________________________________________________________


def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_accesss_token(pyload):
    return jwt.encode(
        {'exp':datetime.now() + timedelta(minutes=5)},
        settings.SECRET_KEY,
        algorithm='HS256'
    )

def get_refresh_token():
    return jwt.encode(
        {'exp':datetime.now() + timedelta(days=365), 'data': get_random(10)},
        settings.SECRET_KEY,
        algorithm='HS256'
    )

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['email'], 
            password=serializer.validated_data['password'],  
            )

        if not user:
            return Response({'error':'Invalid email or password'}, status='400')
        
        access = get_accesss_token({ 'user_id': user.id })
        refresh = get_refresh_token()

        jwt.objects.create(
            user_id = user.id,
            access=access,
            refresh=refresh
        )

        return Response({'access': access, 'refresh': refresh,})

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raisE_exception=True)

        CustomUser.objects._create_user(**serializer.validated_data)

        return Response({"success": 'user created'})
