from django.db import models
from .category import Category
from core.models.school import Department
from ..base import ACCESS_LEVEL_CHOICES

class Library(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    target = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='libraries')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='libraries')
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVEL_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Libraries"
