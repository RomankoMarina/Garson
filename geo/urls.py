from django.urls import path,include,re_path
from geo.views.regions import regions
from geo.views.cities import cities
from geo.views.streets import streets
from place.views.places import places
from django.apps import apps

urlpatterns = [
    re_path(r'regions/$', regions, name='regions'),
    re_path(r'cities/$', cities, name='cities'),
    re_path(r'streets/$', streets, name='streets'),
    re_path(r'places/$', places, name='places'),
]