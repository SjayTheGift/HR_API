from django.urls import path
from .views import (
    LogInView, 
    EmployeeListView,
    EmployeeSignUpView,
    EmployeeDetailView,
    DepartmentListCreateView,
    DepartmentDetailView,
    DesignationListCreateView,
    DesignationDetailView,
    CountUserAndDepartmentView,
)

urlpatterns = [
    # path('admin/', admin.site.urls),
      path('api/user/login/', LogInView.as_view(), name='login'),
      path('api/user/employee/', EmployeeListView.as_view(), name='employee'),
      path('api/user/employee/create/', EmployeeSignUpView.as_view(), name='employee_create'),
      path('api/user/employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
      path('api/user/department/', DepartmentListCreateView.as_view(), name='department'),
      path('api/user/department/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
      path('api/user/designation/', DesignationListCreateView.as_view(), name='designation'),
      path('api/user/designation/<int:pk>/', DesignationDetailView.as_view(), name='designation_detail'),
      path('api/data/count/', CountUserAndDepartmentView.as_view(), name='data_count'),
]
