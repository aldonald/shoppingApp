from rest_framework_json_api import serializers
from server.models import ShoppingList, ShoppingItem
from drf_extra_fields.fields import Base64ImageField

class ShoppingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = (
            'name',
            'user',
        )


class ShoppingItemSerializer(serializers.ModelSerializer):
    included_serializers = {
        'shopping_list': 'server.api.serializers.ShoppingListSerializer',
    }

    class Meta:
        model = ShoppingItem
        fields = (
            # Attributes
            'name',
            'image',
            'price',

            # Foreign Key
            'shopping_list',
        )
