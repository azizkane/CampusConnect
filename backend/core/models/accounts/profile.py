from django.db import models
from .user import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    preferences = models.JSONField(default=dict, blank=True) 

    class Meta:
        verbose_name_plural = "User Profiles"
        
    def __str__(self):
        return f"Profile of {self.user.get_full_name()}"
    
    def get_avatar(self):
        return self.avatar
    
    """
    def get_bio(self):
        return self.bio
    
    def get_preferences(self):
        return self.preferences

    def get_user(self):
        return self.user

    def get_user_id(self):
        return self.user.id
    
    def get_user_first_name(self):
        return self.user.first_name
    
    def get_user_last_name(self):
        return self.user.last_name

    def get_user_email(self):
        return self.user.email

    def get_user_username(self):
        return self.user.username

    def get_user_is_active(self):
        return self.user.is_active

    def get_user_is_staff(self):
        return self.user.is_staff

    def get_user_is_superuser(self):
        return self.user.is_superuser

    def get_user_last_login(self):
        return self.user.last_login
"""

