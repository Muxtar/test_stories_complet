from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     image = models.ImageField(upload_to='profile/', blank=True, default='default.avif')

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', default='profile/default.png')
    
    def __str__(self) -> str:
        return self.user.username
    
class BlockUser(models.Model):
    user = models.ForeignKey(User, related_name='block', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username
    
class Ip(models.Model):
    users = models.ManyToManyField(User, related_name='ip')
    ip = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.ip}'