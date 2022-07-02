from django.db import models
from rarerestapi.models.post import Post
from rarerestapi.models.rareuser import RareUser
from rarerestapi.models.reaction import Reaction


class PostReaction(models.Model):

    user = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)  
  