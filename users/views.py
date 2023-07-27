from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView # new
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
from .serializers import (
    LogInSerializer, 
    UserDisplaySerializer,
    UserCreateSerializer,
    DepartmentSerializer,
    DesignationSerializer,
    )
from .models import Employee, Department, Designation

User = get_user_model()

class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = UserDisplaySerializer
    

class EmployeeSignUpView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = UserCreateSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = UserCreateSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DesignationListCreateView(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class DesignationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
