from django.db import models
from base.models import BaseModel


class Feature(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)