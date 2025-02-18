from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Log(models.Model):
    ACTION = (
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
        ('OTHER', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255, choices=ACTION)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"
