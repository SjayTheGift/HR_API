from django.contrib import admin
from .models import LeaveType, LeaveApplication, LeaveBalance


admin.site.register(LeaveType)
admin.site.register(LeaveApplication)
admin.site.register(LeaveBalance)
