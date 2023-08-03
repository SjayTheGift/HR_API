from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework.reverse import reverse
import time

from .models import Employee, Department, Designation

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password':{'write_only': True, 'required': True}
        }

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name',)


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('id','name', )


class UserDisplaySerializer(serializers.ModelSerializer):
    department = serializers.CharField()
    designation = serializers.CharField()
    class Meta:
        model = Employee
        fields = ('id', 'email', 'first_name', 'last_name', 'department', 'designation', 'phone', 'gender', 'birth_date')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_query = User.objects.filter(email=user)
        data_dict = [{'email': i.email, 'is_hr': i.is_hr, 'is_employee': i.is_employee, 'first_name': i.first_name} for i in user_query]
        email = data_dict[0]['email']
        is_hr = data_dict[0]['is_hr']
        is_employee = data_dict[0]['is_employee']
        first_name = data_dict[0]['first_name']
        
        print(user_query)

        user_data = {'email': str(email), 'is_hr': str(is_hr), 'is_employee': str(is_employee), 'first_name': str(first_name)}

        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token
