from django.db import models
from rarerestapi.models.rareuser import RareUser


class Subscription(models.Model):

    author = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    follower = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="following")
    created_on = models.DateField()
    deleted_on = models.DateField()
  
