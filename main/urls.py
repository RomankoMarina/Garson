from django.urls import path,include,re_path
from main.views.hello import hello


urlpatterns = [
    re_path(r'$', hello, name='hello'),]