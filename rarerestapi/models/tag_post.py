from django.db import models
from rarerestapi.models  import Post, Tag

class TagPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)