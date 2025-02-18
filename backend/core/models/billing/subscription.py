from django.db import models
from core.models.school.app import School
from .plan import Plan

class Subscription(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Expired', 'Expired'),
        ('Cancelled', 'Cancelled'),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school_name')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, related_name='school_chosen_plan')
    start_date = models.DateField()
    end_date = models.DateField()
    student_count = models.PositiveIntegerField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.school.name} - {self.plan.name}"
