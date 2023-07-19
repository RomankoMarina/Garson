from django.db import models
from base.models import BaseModel


class Meal(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    category = models.ForeignKey("menu.Category", related_name='meals', on_delete=models.DO_NOTHING,blank=True,null=True)
    place = models.ForeignKey("place.Place", related_name='meals', on_delete=models.CASCADE)
    features = models.ManyToManyField("menu.Feature", related_name='meals',blank=True,null=True)