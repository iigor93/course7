from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    default_password = models.CharField(max_length=20, default='qwerty123')
