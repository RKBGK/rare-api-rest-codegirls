from django.db import models as model
from rarerestapi.models.category import Category
from rarerestapi.models.rareuser import RareUser
from rarerestapi.models.tag import Tag


class Post(model.Model):
    user = model.ForeignKey(RareUser,on_delete=model.CASCADE )
    category = model.ManyToManyField(Category)
    title = model.CharField(max_length=50)
    publication_date = model.DateField()
    image_url = model.URLField(max_length=500, default=None)
    content = model.CharField(max_length=500)
    approved = model.CharField(max_length=50)
    posttag = model.ManyToManyField(Tag)
    