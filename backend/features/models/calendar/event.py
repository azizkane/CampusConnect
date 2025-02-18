from django.db import models
from django.conf import settings
from core.models.school import School, Department, Classroom
from ..base import CATEGORY_CHOICES
from django.utils import timezone

class Event(models.Model):
    TYPE_CHOICES = [
        ('Class', 'Class'),
        ('Exam', 'Exam'),
        ('Meeting', 'Meeting'),
        ('Activity', 'Activity'),
        ('Project', 'Project'),
        ('Holiday', 'Holiday'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='events')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='organized_events')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=False, blank=False, default='default')
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    place = models.CharField(max_length=255, blank=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events')
    is_recurring = models.BooleanField(default=False)
    recurrence_pattern = models.JSONField(default=dict, blank=True)
    reminder_settings = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


    def duration(self):
        return self.end_datetime - self.start_datetime
