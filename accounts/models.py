from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')
  nickname = models.CharField(max_length=20)

  def __str__(self):
    return self.nickname
