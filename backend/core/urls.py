from django.urls import path, include
from .views import *

# Account URLs
users_patterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

profile_patterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('users/<int:user_pk>/profile/', UserProfileView.as_view(), name='user-profile-by-user'),
]

account_patterns = [
    path('', include(users_patterns)),
    path('', include(profile_patterns)),
]

# Billing URLs
billing_patterns = [
    path('plans/', PlanListCreateView.as_view(), name='plan-list-create'),
    path('plans/<int:pk>/', PlanDetailView.as_view(), name='plan-detail'),
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('subscriptions/<int:pk>/', SubscriptionDetailView.as_view(), name='subscription-detail'),
]

school_patterns =[
    path('schools/', SchoolListCreateView.as_view(), name='superadmin-school-list-create'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='superadmin-school-detail'),
]
# School URLs
school_detailed_patterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('managers/', ManagerListCreateView.as_view(), name='manager-list-create'),
    path('managers/<int:pk>/', ManagerDetailView.as_view(), name='manager-detail'),
    path('classrooms/', ClassroomListCreateView.as_view(), name='classroom-list-create'),
    path('classrooms/<int:pk>/', ClassroomDetailView.as_view(), name='classroom-detail'),
]

# Student URLs
students_patterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]

# Team URLs
team_patterns = [
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]


core_superadmin_patterns = [
    path('', include(school_patterns)),
    path('billing/', include(billing_patterns)),
    path('schools/<int:school_pk>/', include(
        users_patterns 
        + students_patterns
        + team_patterns
        + school_detailed_patterns
    )),
]

# Main URL patterns ################################################
urlpatterns = [
    path('', include(account_patterns)),
    path('', include(school_detailed_patterns)),
    path('', include(students_patterns)),
    path('', include(team_patterns)),
]
####################################################################


