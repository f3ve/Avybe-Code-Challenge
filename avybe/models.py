from django.db import models

class UserProfile(models.Model):
  username = models.TextField()
  profile_img = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.nickname
  