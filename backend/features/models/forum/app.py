from django.db import models
from django.conf import settings
from core.models.school import School, Department

class Forum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='forums')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='forums')
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='moderated_forums')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title