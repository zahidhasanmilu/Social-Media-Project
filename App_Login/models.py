from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='Profile_Pic')
    dob = models.DateTimeField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    
    
