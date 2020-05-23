from django.db import models
from decimal import Decimal


class ShoppingList(models.Model):
    name = models.CharField(max_length=40)


class ShoppingItem(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    barcode = models.CharField(max_length=100, default='', blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, default=Decimal(0), blank=True, null=True)
    shopping_list = models.ForeignKey(
        ShoppingList, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
