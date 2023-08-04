from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

class LeaveType(models.Model):
    title = models.CharField(max_length=200)
    number_of_leaves_per_year = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LeaveApplication(models.Model):
    class Status(models.TextChoices):
        Pending = 'pending'
        Approved = 'approved'
        Rejected = 'rejected'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name='leave_type')
    from_date = models.DateField(help_text='leave start date is on ..')
    to_date = models.DateField(help_text='coming back on ...')
    reason = models.TextField()
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.Pending)
    date_of_approval = models.DateField(auto_now=True)
    is_approved = models.BooleanField(default=False) #hide

    
    def __str__(self):
        return f'{self.leave_type.title} - {self.user}'

    @property
    def leave_days(self):
        start_date = self.from_date
        end_date = self.to_date
        if start_date > end_date:
            return 0
        dates = (end_date - start_date)
        return dates.days

    @property
    def unapproved_leave(self):
        if self.is_approved:
            self.is_approved = False
            self.status = 'new'
            self.save()

    @property
    def approve_leave(self):
        if not self.is_approved:
            self.is_approved = True
            self.status = 'approved'
            self.save()
    
    @property
    def reject_leave(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'rejected'
            self.save()


class LeaveBalance(models.Model):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name='leave_type_balance')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_allocation')
    number_of_days = models.PositiveIntegerField(default=0)
    date_created = models.DateField(auto_now=True)
    # days_taken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.leave_type.title} - {self.number_of_days}'


def create_leave_balance(sender, instance, created, **kwargs):
    leave_types = LeaveType.objects.all()
    if created:
        for data in leave_types:
            leave_balance = LeaveBalance(user=instance, leave_type=data, number_of_days=data.number_of_leaves_per_year)
            leave_balance.save()

post_save.connect(create_leave_balance, sender=User)

    