from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')
  nickname = models.TextField()
  
  def get_absolute_url(self):
    return reverse('createProfile', kwargs={'pk': self.pk})
