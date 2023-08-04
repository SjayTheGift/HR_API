from django.urls import path
from .views import (
    LeaveTypeListCreateView,
    LeaveTypeDetailView,
    PendingLeavesView,
    PendingLeavesUpdateView,
    LeaveBalanceView,
    # UserLeavesView,
    # UserCreateLeavesView,
    # CountUserAndDepartmentView
)

urlpatterns = [
    path('api/leave/leave-type/', LeaveTypeListCreateView.as_view(), name='leave_type'),
    path('api/leave/leave-type/<int:pk>/', LeaveTypeDetailView.as_view(), name='leave_type_detail'),
    path('api/leave/leave-pending/', PendingLeavesView.as_view(), name='leave_pending'),
    path('api/leave/leave-pending/<int:pk>/', PendingLeavesUpdateView.as_view(), name='leave_pending_update'),
    path('api/leave/leave-balance/', LeaveBalanceView.as_view(), name='leave_balance'),
    # path('api/leave/user-leave/', UserLeavesView.as_view(), name='user_leave'),
    # path('api/leave/user-leave/application/', UserCreateLeavesView.as_view(), name='user_leave_application'),
    # path('api/data/count/', CountUserAndDepartmentView.as_view(), name='data_count'),
    # path('api/login/', LogInView.as_view(), name='login'),
]
