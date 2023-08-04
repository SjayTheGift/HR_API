from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView # new
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
from .serializers import (
    LogInSerializer, 
    UserDisplaySerializer,
    UserSerializer,
    DepartmentSerializer,
    DesignationSerializer,
    )
from .models import Department, Designation

User = get_user_model()

class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDisplaySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes  = (IsAuthenticated)

    

class EmployeeSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (IsAuthenticated)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (IsAuthenticated)


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_class = (IsAuthenticated)


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (IsAuthenticated)


class DesignationListCreateView(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (IsAuthenticated)


class DesignationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (IsAuthenticated)
