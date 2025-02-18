from django.db import models
from django.conf import settings
from core.models.school import School
from ..base import ACCESS_LEVEL_CHOICES

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='managed_categories')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='library_categories')
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVEL_CHOICES)
    target = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"