from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def total_users():
        return User.objects.count()


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    class GenderType(models.TextChoices):
        Male = 'Male'
        Female = 'Female'
        
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='department')
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING, related_name='designation')
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=50, choices=GenderType.choices, default=GenderType.Male)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    
    

    
    # @receiver(post_save, sender = User)
    # def create_employee(sender,instance,created,**kwargs):
    #     if created:
    #         Employee.objects.create(user=instance)

    # @receiver(post_save, sender = User)
    # def save_employee(sender,instance,created,**kwargs):
    #     if instance.is_employee:
    #         instance.employee.save()
    