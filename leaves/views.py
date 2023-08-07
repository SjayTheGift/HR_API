from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from django.http import Http404
from django.conf import settings

from django.contrib.auth import get_user_model

from .models import LeaveType, LeaveApplication, LeaveBalance
from .serializers import (
    LeaveTypeSerializer, 
    LeaveApplicationSerializer,
    LeaveAllocationSerializer,
    LeaveApplicationCreateSerializer,
    )

User = get_user_model()

class LeaveTypeListCreateView(generics.ListCreateAPIView):
    """
        Create and return a list of all Leave Types.
    """
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer


class LeaveTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update and delete a single Leave Type.
    """
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer


class UserCreateLeavesView(APIView):
 
    def post(self, request, format=None):
        serializer = LeaveApplicationCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLeavesApplicationView(APIView):
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
        
        queryset = LeaveApplication.objects.filter(user=user_id)
        serializer = LeaveApplicationSerializer(queryset, many=True)
        return Response(serializer.data)


class LeaveBalanceView(APIView):
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
        
        queryset = LeaveBalance.objects.filter(user=user_id)
        serializer = LeaveAllocationSerializer(queryset, many=True)
        return Response(serializer.data)



class PendingLeavesView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users with pending leaves to approve.
        """
        queryset = LeaveApplication.objects.filter(status='pending')
        serializer = LeaveApplicationSerializer(queryset, many=True)
        return Response(serializer.data)


class PendingLeavesUpdateView(generics.RetrieveUpdateAPIView):
    """
        Update pending leaves for user with reject or approve.
    """
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

