from django.db import models
from django.conf import settings
from core.models.students import Team
from ..base import CATEGORY_CHOICES

class Project(models.Model):
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('Active', 'Active'),
        ('OnHold', 'OnHold'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='projects')
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='supervised_projects')
    place = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Planning')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=False, blank=False, default='Project')
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def calculate_progress(self):
        total_tasks = self.tasks.count()
        if total_tasks == 0:
            return 0
        completed_tasks = self.tasks.filter(status='Completed').count()
        return (completed_tasks / total_tasks) * 100


