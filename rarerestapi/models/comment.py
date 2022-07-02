from django.db import models
from rarerestapi.models.post import Post
from rarerestapi.models.rareuser import RareUser


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(RareUser, on_delete=models.CASCADE)    
    content = models.CharField(max_length=500)
    created_on = models.DateField()
  