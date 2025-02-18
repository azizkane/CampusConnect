from django.db import models

class Plan(models.Model):
    BILLING_CYCLE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Yearly', 'Yearly'),
    ]

    name = models.CharField(max_length=255)
    max_students = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    billing_cycle = models.CharField(max_length=10, choices=BILLING_CYCLE_CHOICES)
    is_calendar_enabled = models.BooleanField(default=True)
    is_forum_enabled = models.BooleanField(default=True)
    is_library_enabled = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
