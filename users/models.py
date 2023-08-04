import datetime
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# from django.dispatch import receiver
# from django.db.models.signals import pre_save, post_save


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
        extra_fields.setdefault('is_hr', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_hr') is not True:
            raise ValueError(_('Superuser must have is_hr=True.'))
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    class GenderType(models.TextChoices):
        Male = 'Male'
        Female = 'Female'
        Other = 'other'
        Not_Known = 'Not Known'

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    start_date = models.DateField(_('Employment Date'),help_text='date of employment',blank=False,null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='department', null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, related_name='designation', null=True, blank=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=50, choices=GenderType.choices, default=GenderType.Male)
    date_of_birth = models.DateField(null=True, blank=True)
    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True,null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        fullname = ''
        firstname = self.first_name
        lastname = self.last_name
        middle_name = self.middle_name

        if (firstname and lastname) or middle_name is None:
            fullname = f'{firstname} {lastname}'
            return fullname
        elif middle_name:
            fullname = f'{firstname} {lastname} {middle_name}'
            return fullname
        return

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        date_of_birth_year = self.date_of_birth.year
        if date_of_birth_year:
            return current_year - date_of_birth_year
        return
    