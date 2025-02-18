from django.db import models
from core.models.school import Department
from  core.models.accounts import User

class Classroom(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='classes')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes_supervised')
    students = models.ManyToManyField('core.Student', related_name='classes_enrolled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.department.name}"
    
    def get_students(self):
        return self.students.all()

    def get_supervisor(self):
        return self.supervisor

    def get_department(self):
        return self.department

    def get_class_name(self):
        return self.name

    def get_class_id(self):
        return self.id

    def get_class_created_at(self):
        return self.created_at

    def get_class_updated_at(self):
        return self.updated_at

    def get_class_students(self):
        return self.students.all()

    def get_class_supervisor(self):
        return self.supervisor

    def get_class_department(self):
        return self.department

    def get_class_name(self):
        return self.name

    def get_class_id(self):
        return self.id

    def get_class_created_at(self):
        return