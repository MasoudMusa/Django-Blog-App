from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class BlogStuff(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=100, default='This is the description...')
    date_published = models.DateField(default=datetime.now, blank=True)
    post_image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.user.username