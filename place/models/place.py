from django.db import models
from base.models import BaseModel


class Place(BaseModel):
    class Type(models.IntegerChoices):
        RES = 1, "Ресторан"
        CAFE = 2, "Кафе"
        BAR = 3, "Бар"

    name = models.CharField(max_length=100)
    type = models.SmallIntegerField(choices=Type.choices,default=Type.RES)
    phone_number = models.CharField(max_length=100,blank=True,null = True)
    email = models.EmailField(blank=True,null = True)
    street = models.ForeignKey("geo.Street",related_name='places',on_delete=models.DO_NOTHING,blank=True,null = True)
    building = models.CharField(max_length=100,blank=True,null = True)
    coordinate = models.CharField(max_length=100,blank=True,null = True)
    logo = models.FileField(upload_to='logo',blank=True,null = True)
    description = models.TextField(blank=True,null = True)
