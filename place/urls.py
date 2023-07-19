from django.urls import path,include,re_path
from place.views.places import places,place_edit,place_delete


urlpatterns = [
    re_path(r'place/$', places, name='places'),
    re_path(r'^place/(?P<nn>[-\w]+)/edit/$', place_edit,name='place_edit'),
    re_path(r'^place/(?P<nn>[-\w]+)/delete/$', place_delete,name='place_delete'),

]

