from django.db import models
from rarerestapi.models.post import Post
from rarerestapi.models.rareuser import RareUser
from rarerestapi.models.reaction import Reaction


class PostReaction(models.Model):

    user_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction_id = models.ForeignKey(Reaction, on_delete=models.CASCADE)  
  