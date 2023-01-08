from django.db import models

# Create your models here.

class myappModel(models.Model):
    image_title = models.CharField(max_length=100)
    image_description = models.CharField(max_length=1000)
    image_photo = models.ImageField(upload_to = 'profile_image/')