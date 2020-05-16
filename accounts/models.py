from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username
