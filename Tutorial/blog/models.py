from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    game = models.CharField(max_length=100)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.game

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})