from django.db import models 
from rarerestapi.models.category import Category
from rarerestapi.models.rareuser import RareUser
from rarerestapi.models.tag import Tag


class Post(models.Model):

    user = models.ForeignKey(RareUser, on_delete=models.CASCADE)    
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.URLField(max_length=500, default=None)
    content = models.CharField(max_length=500)
    approved = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="associatedposts")
    