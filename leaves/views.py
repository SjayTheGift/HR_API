from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http import Http404
from django.conf import settings

from .models import LeaveType, LeaveApplication
from .serializers import LeaveTypeSerializer, LeaveApplicationSerializer

from users.models import Employee

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
    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        current_user = request.user.pk
        # print(request.data)

        # print(current_user)

        # user_agent_info = request.META.get('HTTP_USER_AGENT', 'http://localhost:5173')[:255],
        # print(user_agent_info)

        print(settings.SIMPLE_JWT['USER_ID_FIELD'])

        queryset = LeaveApplication.objects.filter(employee=current_user)
        serializer = LeaveApplicationSerializer(queryset, many=True)
        return Response(serializer.data)

    # def get_object(self, pk):
    #     try:
    #         return LeaveApplication.objects.get(pk=pk)
    #     except LeaveApplication.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     leave = self.get_object(pk)
    #     serializer = LeaveApplicationSerializer(leave)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = LeaveApplicationSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     leave = self.get_object(pk)
    #     leave.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    