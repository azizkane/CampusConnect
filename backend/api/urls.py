"""API (MAIN FILE) URL Configuration
"""
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.urls import core_superadmin_patterns
from system.urls import system_superadmin_patterns

router = DefaultRouter()

# index_patterns = [ 
#     path('', include(router.urls)),
#     path('home/', ),
#     path('dashboard/', ),
#     path('404/', ),
#     path('unauthorized/', ),
# ]

apps_patterns = [
    path('core/', include('core.urls')),      # Core functionality 
    path('features/', include('features.urls')), # Features
    path('system/', include('system.urls')),  # System-level endpoints
]

superadmin_patterns = [
        path('', include(core_superadmin_patterns)),
        path('', include(system_superadmin_patterns)),
]

# path('', include(index_patterns), namespace='index'),
urlpatterns = [
    path('api/', include(apps_patterns)),
    path('admin/', admin.site.urls),
    path('api/admin/', include(superadmin_patterns)),
    
]