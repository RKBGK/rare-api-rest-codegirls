from django.db import models
from rarerestapi.models.rareuser import RareUser


class DemotionQueue(models.Model):

    action = models.CharField(max_length=50)
    admin = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    approver = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name="approving")  
  
