from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    AuthTokenView,
    AuditLogListView,
    # TokenRefreshView,
    # TokenVerifyView,
)

router = DefaultRouter()

auth_patterns = [
    path('token/', AuthTokenView.as_view(), name='token-obtain'),
]

audit_patterns = [
    path('logs/', AuditLogListView.as_view(), name='audit-log-list'),
]


urlpatterns = [
    path('', include(router.urls)),  # Includes URLs from the router
    path('auth/', include(auth_patterns)),  # Includes auth-related URLs
    path('audit/', include(audit_patterns)),  # Includes audit log URLs
]


system_superadmin_patterns = [
    path('schools/<int:school_pk>/audit/', include(audit_patterns)),
]


