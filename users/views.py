from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView # new
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
from .serializers import (LogInSerializer, )

User = get_user_model()

class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer