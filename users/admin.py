from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Employee, Designation, Department

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_hr', 'is_employee', )
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_hr', 'is_employee',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_hr', 'is_employee' , )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_hr', 'is_employee',)}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'is_hr', 'is_employee', )
    ordering = ('email', 'first_name', 'last_name',)

admin.site.register(User, CustomUserAdmin)

admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Department)