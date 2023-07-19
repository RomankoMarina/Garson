from django.db import models

from django.contrib.auth.models import AbstractUser
from base.models import BaseModel

class User(AbstractUser,BaseModel):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    class Meta:
        db_table = 'auth_user'
        # swappable = "AUTH_USER_MODEL"


