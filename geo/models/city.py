from django.db import models
from base.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=50)
    region = models.ForeignKey("geo.Region",related_name='cities',on_delete=models.DO_NOTHING)

