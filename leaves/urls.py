from django.urls import path
from .views import (
    LeaveTypeListCreateView,
    LeaveTypeDetailView,
    NewLeavesView,
    NewLeavesDetailView,
    UserLeavesView
)

urlpatterns = [
    path('api/leave/leave-type/', LeaveTypeListCreateView.as_view(), name='leave_type'),
    path('api/leave/leave-type/<int:pk>/', LeaveTypeDetailView.as_view(), name='leave_type_detail'),
    path('api/leave/leave-new/', NewLeavesView.as_view(), name='leave_type_new'),
    path('api/leave/leave-new/<int:pk>/', NewLeavesDetailView.as_view(), name='leave_type_detail'),
    path('api/leave/user-leave/', UserLeavesView.as_view(), name='user_leave'),
    # path('api/login/', LogInView.as_view(), name='login'),
]
