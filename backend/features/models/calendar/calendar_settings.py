from django.db import models
from django.conf import settings


class CalendarSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='calendar_settings')
    default_view = models.CharField(max_length=50, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month')], default='Month')
    timezone = models.CharField(max_length=100, default='UTC')
    notifications_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"Calendar Settings for {self.user.get_full_name()}"
    
    def save(self, *args, **kwargs):
        # Ensure that only one instance of CalendarSettings exists for each user
        if not self.pk and CalendarSettings.objects.filter(user=self.user).exists():
            raise ValueError("A CalendarSettings instance already exists for this user.")
        super().save(*args, **kwargs)
        
    def get_default_view(self):
        return self.default_view

    def get_timezone(self):
        return self.timezone

    def get_notifications_enabled(self):
        return self.notifications_enabled

    def get_created_at(self):
            return self.created_at

    def get_updated_at(self):
            return self.updated_at

    class Meta:
        verbose_name_plural = "Calendar Settings"