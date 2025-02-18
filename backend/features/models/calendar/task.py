from django.db import models
from django.conf import settings
from .project import Project
from django.utils import timezone




class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='tasks')
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def is_overdue(self):
        return self.due_date < timezone.now().date() and self.status != 'Completed'
    
    def is_completed(self):
        return self.status == 'Completed'
    
    def assign_task(self, user):
        self.assigned_to = user
        self.save()
        
    # def save(self):
    #     if self.due_date < timezone.now().date() and self.status != 'Completed':
    #         self.status = 'Pending'
    #     super().save()
