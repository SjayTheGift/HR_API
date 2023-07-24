from django.db import models


class LeaveType(models.Model):
    title = models.CharField(max_length=200)
    days = models.IntegerField()


class LeaveApplication(models.Model):
    class Status(models.TextChoices):
        New = 'new'
        Approved = 'approved'
        Rejected = 'rejected'

    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField()
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.New)
   