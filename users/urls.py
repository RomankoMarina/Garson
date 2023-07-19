from django.urls import path,include,re_path
from users.views.users import users



urlpatterns = [
    re_path(r'users/$', users, name='users'),]