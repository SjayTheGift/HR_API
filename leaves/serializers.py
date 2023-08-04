from rest_framework import serializers
from .models import LeaveType, LeaveApplication, LeaveBalance
from django.contrib.auth import get_user_model

from users.models import Department

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'full_name')


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = ('id', 'title', 'number_of_leaves_per_year')


class LeaveAllocationSerializer(serializers.ModelSerializer):
    # leave_type = LeaveTypeSerializer()
    class Meta:
        model = LeaveBalance
        fields = ('number_of_days', 'leave_type', 'user')


class LeaveApplicationSerializer(serializers.ModelSerializer):
    # employee = UserSerializer()
    # leave_type = LeaveTypeSerializer()
    class Meta:
        model = LeaveApplication
        fields = ('id', 'from_date', 'to_date', 'reason', 'date_applied', 'status', 'leave_days', 'leave_type', 'user')
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status')
        instance.user = validated_data.get('user')
        instance.leave_type = validated_data.get('leave_type')

        obj_data = LeaveBalance.objects.filter(user=instance.user, leave_type=instance.leave_type)

 
        for i in obj_data:
            if (instance.status == 'approved'):
                days_left = i.number_of_days - instance.leave_days
                i.number_of_days = days_left
                i.save()
                
        instance.save()
        return instance


# class LeaveApplicationCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LeaveApplication
#         fields = ('id', 'from_date', 'to_date', 'description', 'date_applied', 'employee', 'leave')

#     def create(self, validated_data):
#         leave_application = LeaveApplication.objects.create(**validated_data)
#         return leave_application



# class CountUserAndDepartment(serializers.Serializer):
#     total_users = serializers.SerializerMethodField()
#     total_pending_leave = serializers.SerializerMethodField()
#     total_department = serializers.SerializerMethodField()
    
#     class Meta:
#         fields = ('total_pending_leave', 'total_department', 'total_users',)
    
#     def get_total_users(self, obj):
#         data = User.objects.count()
#         return data

#     def get_total_pending_leave(self, obj):
#         data = LeaveApplication.objects.filter(status='new').count()
#         return data

#     def get_total_department(self, obj):
#         data = Department.objects.filter().count()
#         return data
        