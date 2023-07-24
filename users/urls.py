from django.urls import path
from .views import (
    LogInView
)

urlpatterns = [
    # path('admin/', admin.site.urls),
      path('api/login/', LogInView.as_view(), name='login'),
]
