from django.db import models
from django.conf import settings
from core.models.school import Department, Classroom

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='student_department')
    father_full_name = models.CharField(max_length=200, null=True)
    mother_full_name = models.CharField(max_length=200, null=True)
    father_email = models.EmailField(null=True)
    mother_email = models.EmailField(null=True)
    enrollment_class = models.ForeignKey(Classroom, on_delete=models.CASCADE, max_length=100, related_name='student_classroom', null=True)
    enrollment_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    ROLE_CHOICES = [
        ('Leader', 'Leader'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Graduated', 'Graduated'),
        ('Suspended', 'Suspended'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')


    def __str__(self):
        return f"{self.user.get_full_name()} - {self.student_id}"
