from django.db import models
from django.conf import settings

class SharedCalendar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_calendars')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_calendars')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['owner']),
            models.Index(fields=['name']),
        ]
        verbose_name_plural = "Shared Calendars"
