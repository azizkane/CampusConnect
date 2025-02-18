from django.db import models
from django.db import models
from core.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey('core.School', on_delete=models.CASCADE, related_name='manager_school_origin', null=True, blank=True)
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE, related_name='manager_department_origin', null=True, blank=True)
    permissions = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['school', 'department']),
            models.Index(fields=['user', 'is_active']),
        ]

    def __str__(self):
        return f"Manager: {self.user.get_full_name()} - {self.school.name}"

    @property
    def has_calendar_access(self):
        return self.permissions.get('calendar', False)

    @property
    def has_library_access(self):
        return self.permissions.get('library', False)

    @property
    def has_forum_access(self):
        return self.permissions.get('forum', False)

    @property
    def has_projects_access(self):
        return self.permissions.get('projects', False)


class ActiveUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
