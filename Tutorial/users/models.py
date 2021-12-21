from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F
from django.db.models.fields.related import OneToOneField
from PIL import Image

class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            img_size = (300, 300)
            img.thumbnail(img_size)
            img.save(self.image.path)