from django.contrib import admin
from .models import ShoppingList, ShoppingItem


@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    pass

# Register your models here.
