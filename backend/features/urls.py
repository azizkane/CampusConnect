from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

calendar_patterns = [
        path('', SharedCalendarListCreateView.as_view(), name='shared-calendar-list-create'),
        path('<int:pk>/', SharedCalendarDetailView.as_view(), name='shared-calendar-detail'),
        path('settings/', CalendarSettingsListCreateView.as_view(), name='calendar-settings-list-create'),
        path('settings/<int:pk>/', CalendarSettingsDetailView.as_view(), name='calendar-settings-detail'),
        path('events/', EventListCreateView.as_view(), name='event-list-create'),
        path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
        path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
        path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
        path('projects/<int:project_pk>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
        path('projects/<int:project_pk>/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]

forums_patterns = [
        path('', ForumListCreateView.as_view(), name='forum-list-create'),
        path('<int:pk>/', ForumDetailView.as_view(), name='forum-detail'),
        path('topics/', TopicListCreateView.as_view(), name='topic-list-create'),
        path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
        path('posts/', PostListCreateView.as_view(), name='post-list-create'),
        path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]

library_patterns = [
        path('', LibraryListCreateView.as_view(), name='library-list-create'),
        path('<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
        path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
        path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
        path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
        path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
]

urlpatterns = [
        path('calendar/', include(calendar_patterns)),
        path('forums/', include(forums_patterns)),
        path('library/', include(library_patterns)),
]