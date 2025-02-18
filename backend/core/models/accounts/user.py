from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models.base import UserManager, BaseUser
from django.db import models

class User(AbstractBaseUser, PermissionsMixin, BaseUser):
    ROLE_CHOICES = [
        ('SuperAdmin', 'SuperAdmin'),
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Student', 'Student'),
        ('Parent', 'Parent'),
        ('Teacher', 'Teacher'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128, null=True)  # Temporarily allow null
    profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE, null=True, related_name='user_profile')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
            models.Index(fields=['is_active']),
        ]
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    