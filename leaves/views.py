from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from django.http import Http404
from django.conf import settings

from django.contrib.auth import get_user_model

from .models import LeaveType, LeaveApplication
from .serializers import (
    LeaveTypeSerializer, 
    LeaveApplicationSerializer,
    LeaveApplicationCreateSerializer,
    CountUserAndDepartment
    )

from users.models import Employee


User = get_user_model()

class LeaveTypeListCreateView(generics.ListCreateAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer


class LeaveTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer


class NewLeavesView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = LeaveApplication.objects.filter(status='new')
        serializer = LeaveApplicationSerializer(queryset, many=True)
        return Response(serializer.data)


class NewLeavesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer


class UserLeavesView(APIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        # current_user = request.user.pk
        user_id = request.META.get('HTTP_AUTHORIZATION')

        # data = {'token': token}
        # valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        # user = valid_data['user']
        # request.user = user
        
        queryset = LeaveApplication.objects.filter(employee=user_id)
        serializer = LeaveApplicationSerializer(queryset, many=True)
        return Response(serializer.data)
    


class UserCreateLeavesView(APIView):
 
    def post(self, request, format=None):
        serializer = LeaveApplicationCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountUserAndDepartmentView(APIView):
    
    def get(self, request, *args, **kwargs):
        data = [{"data": 0,}]
        serializer = CountUserAndDepartment(data, many=True)
        return Response(serializer.data)