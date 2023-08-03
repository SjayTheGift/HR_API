from rest_framework import serializers
from .models import LeaveType, LeaveApplication
from django.contrib.auth import get_user_model

from users.models import Department

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'full_name')
    
    def get_full_name(self, obj):
        return f'{obj.first_name}{obj.last_name}'


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'


class LeaveApplicationSerializer(serializers.ModelSerializer):
    employee = UserSerializer()
    leave = LeaveTypeSerializer()
    class Meta:
        model = LeaveApplication
        fields = ('id', 'from_date', 'to_date', 'description', 'date_applied', 'status', 'leave', 'employee')
    
    def update(self, instance, validated_data):
        print()
        instance.status = validated_data.get('status')

        instance.save()
        return instance


class LeaveApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = ('id', 'from_date', 'to_date', 'description', 'date_applied', 'employee', 'leave')

    def create(self, validated_data):
        leave_application = LeaveApplication.objects.create(**validated_data)
        return leave_application



class CountUserAndDepartment(serializers.Serializer):
    total_users = serializers.SerializerMethodField()
    total_pending_leave = serializers.SerializerMethodField()
    total_department = serializers.SerializerMethodField()
    
    class Meta:
        fields = ('total_pending_leave', 'total_department', 'total_users',)
    
    def get_total_users(self, obj):
        data = User.objects.count()
        return data

    def get_total_pending_leave(self, obj):
        data = LeaveApplication.objects.filter(status='new').count()
        return data

    def get_total_department(self, obj):
        data = Department.objects.filter().count()
        return data
        