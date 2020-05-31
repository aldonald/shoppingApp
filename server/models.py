from django.db import models
from decimal import Decimal
from accounts.models import User


class ShoppingItem(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, default=Decimal(0), blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
