from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseUser(TimeStampedModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True)
    adress = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save(update_fields=['last_login'])
        
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
        
    def restore(self, *args, **kwargs):
        self.is_active = True
        self.save()
        
    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        
    

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'SuperAdmin')
        return self.create_user(email, password, **extra_fields)
