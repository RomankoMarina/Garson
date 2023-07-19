from django.db import models
from base.models import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=20)

