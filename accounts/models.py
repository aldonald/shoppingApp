from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

class AccountToken(models.Model):
    firebaseToken = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
