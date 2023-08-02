from rest_framework import serializers
from .models import LeaveType, LeaveApplication
from django.contrib.auth import get_user_model

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

# class LeaveApplicationUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LeaveApplication
#         fields = ('id', 'from_date', 'to_date', 'description', 'date_applied', 'status')

