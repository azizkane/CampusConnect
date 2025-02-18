from django.db import models
from .app import Student
from core.models.school import Department


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')
    leader = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='leading_teams')
    members = models.ManyToManyField(Student, related_name='teams')
    is_active = models.BooleanField(default=True)
    max_members = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_full(self):
        return self.members.count() >= self.max_members
