from django.db import models
from django.conf import settings
from .app import Forum

class Topic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='topics')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_topics')
    is_pinned = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title