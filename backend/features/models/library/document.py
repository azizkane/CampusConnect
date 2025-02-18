from django.db import models
from django.conf import settings
from .app import Library
from ..base import ACCESS_LEVEL_CHOICES

class Document(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='documents')
    file_path = models.FileField(upload_to='library_documents/')
    file_size = models.PositiveIntegerField()
    file_type = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_documents')
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVEL_CHOICES)
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
