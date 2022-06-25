from django.db import models

class Reaction(models.Model):

    label = models.CharField(max_length=50)
    image_url = models.URLField(max_length=500, default=None)