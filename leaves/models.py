from django.db import models
from django.contrib.auth import get_user_model

from users.models import Employee

User = get_user_model()

class LeaveType(models.Model):
    title = models.CharField(max_length=200)
    days = models.IntegerField()
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class LeaveApplication(models.Model):
    class Status(models.TextChoices):
        New = 'new'
        Approved = 'approved'
        Rejected = 'rejected'

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    leave = models.ForeignKey(LeaveType, on_delete=models.DO_NOTHING, related_name='leave_type')
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField()
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.New)

    @property
    def get_leave_day(self):
        return self.from_date - self.to_date
    
    def __str__(self):
        return f'{self.leave.title} - {self.employee.first_name} - {self.from_date} - {self.to_date}'
