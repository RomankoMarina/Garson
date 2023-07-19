from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("menu.Category", related_name='categories', on_delete=models.DO_NOTHING,blank=True,null=True)
