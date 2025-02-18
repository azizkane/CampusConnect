from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta


class AuthToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    expiry_date = models.DateTimeField( default=timedelta(days=1))
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_expired(self):
        return timezone.now() > self.expiry_date

    def __str__(self):
        return f"Token for {self.user.email}"

