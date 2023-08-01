from django.contrib import admin
from .models import LeaveType, LeaveApplication


admin.site.register(LeaveType)
admin.site.register(LeaveApplication)
