from django.db import models
from rarerestapi.models.rareuser import RareUser


class Subscription(models.Model):

    author = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="author")
    follower = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="following")
    created_on = models.DateField()
    deleted_on = models.DateField()
  
    @property
    def subscribed(self):
        return self.__subscribed

    @subscribed.setter
    def subscribed(self, value):
        self.__subscribed = value
