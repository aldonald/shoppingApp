from rest_framework_json_api import serializers
from server.models import ShoppingList, ShoppingItem


class ShoppingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = (
            'name',
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
            'barcode',
            'price',

            # Foreign Key
            'shopping_list',
        )
