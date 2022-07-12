from django.db import models
from rarerestapi.models.post import Post
from rarerestapi.models.tag import Tag


class PostTag(models.Model):

    post = models.ManyToManyField(Post)
    tag = models.ManyToManyField(Tag)