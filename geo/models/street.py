from django.db import models
from base.models import BaseModel


class Street(BaseModel):
    name = models.CharField(max_length=50)
    city = models.ForeignKey("geo.City",related_name='streets',on_delete=models.DO_NOTHING)


