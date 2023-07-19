from django.urls import path,include,re_path
from menu.views.categories import categories,category_edit,category_delete
from menu.views.features import features,feature_edit,feature_delete
from menu.views.meals import meals,meal_edit,meal_delete

from django.apps import apps

urlpatterns = [
    re_path(r'categories/$', categories, name='categories'),
    re_path(r'^category/(?P<nn>[-\w]+)/edit/$', category_edit,name='category_edit'),
    re_path(r'^category/(?P<nn>[-\w]+)/delete/$', category_delete,name='category_delete'),
    re_path(r'features/$', features, name='features'),
    re_path(r'^feature/(?P<nn>[-\w]+)/edit/$', feature_edit,name='feature_edit'),
    re_path(r'^feature/(?P<nn>[-\w]+)/delete/$', feature_delete,name='feature_delete'),
    re_path(r'meals/$', meals, name='meals'),
    re_path(r'^meal/(?P<nn>[-\w]+)/edit/$', meal_edit,name='meal_edit'),
    re_path(r'^meal/(?P<nn>[-\w]+)/delete/$', meal_delete,name='meal_delete'),

]