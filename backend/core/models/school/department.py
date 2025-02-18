from django.db import models
from .app import School
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='department')
    head = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='head_department')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} - {self.school.name}"
    
    def get_head(self):
        return self.head
    
    def get_school(self):
        return self.school
    
    def get_description(self):
        return self.description

    def get_is_active(self):
        return self.is_active

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

    def get_departments(self):
        return self.departments.all()

    def get_department_name(self):
        return self.name

    def get_department_id(self):
        return self.id

    def get_department_school(self):
        return self.school

    def get_department_head(self):
        return self.head

    def get_department_description(self):
        return self.description

    def get_department_is_active(self):
        return self.is_active

    def get_department_created_at(self):
        return self.created_at

    def get_department_updated_at(self):
        return self.updated_at
