import time
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

from .models import Department, Designation

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('full_name', 'first_name', 'last_name', 'email', 'middle_name', 'is_hr', 'is_employee', 'start_date', 'department', 'designation', 'phone', 'gender', 'date_of_birth', 'password', 'password2')
        extra_kwargs = {
            'password':{'write_only': True, 'required': True}
        }

    
    def create(self, validated_data):
        user = self.context["request"].user

        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            email=validated_data['email'],
            is_hr=validated_data['is_hr'],
            is_employee=validated_data['is_employee'],
            start_date=validated_data['start_date'],
            department=validated_data['department'],
            designation=validated_data['designation'],
            phone=validated_data['phone'],
            gender=validated_data['gender'],
            date_of_birth=validated_data['date_of_birth'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
    


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
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'middle_name', 'is_hr',  'is_employee', 'start_date', 'department', 'designation', 'phone', 'gender', 'date_of_birth', 'full_name')


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_query = User.objects.filter(email=user)
        data_dict = [{'email': i.email, 'is_hr': i.is_hr, 'is_employee': i.is_employee, 'full_name': i.full_name} for i in user_query]
        email = data_dict[0]['email']
        is_hr = data_dict[0]['is_hr']
        is_employee = data_dict[0]['is_employee']
        full_name = data_dict[0]['full_name']

        user_data = {'email': str(email), 'is_hr': str(is_hr), 'is_employee': str(is_employee), 'full_name': str(full_name)}

        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token
