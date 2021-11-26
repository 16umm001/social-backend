from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from social.base.models import UUIDModel
from social.users.managers import UserManager


class User(AbstractBaseUser, UUIDModel, PermissionsMixin):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, unique=True, db_index=True)
    phone_number = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=128)
    is_active = models.BooleanField("active", default=False)
    is_staff = models.BooleanField("staff status", default=False)

    modified_at = models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username"
    ]
    objects = UserManager()

    def __str__(self):
        return self.email
