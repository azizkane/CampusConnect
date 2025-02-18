from django.db import models
from django.conf import settings
from core.models.billing.plan import Plan

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='school_admin')
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone_number = models.CharField(max_length=20,null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='creation_author') #created_by_superadmin
    is_active = models.BooleanField(default=True)
    current_plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True, related_name='plan')
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)
    settings = models.JSONField(default=dict, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.admin and not self.contact_email:
            self.contact_email = self.admin.email
        if self.admin and not self.contact_phone_number:
            self.contact_phone_number = self.admin.phone_number
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    