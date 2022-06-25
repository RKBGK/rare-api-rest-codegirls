from django.db import models
from django.contrib.auth.models import User


class RareUser(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    image_url = models.URLField(max_length=500, default=None)
    created_on = models.DateField()
    active = models.CharField(max_length=50)