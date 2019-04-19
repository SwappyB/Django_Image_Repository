from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Images(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')

    def save(self):
        super().save()
