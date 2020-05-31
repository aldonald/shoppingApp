from rest_framework_json_api import serializers
from server.models import ShoppingItem

class ShoppingItemSerializer(serializers.ModelSerializer):
    included_serializers = {
        'user': 'server.api.serializers.UserSerializer',
    }

    class Meta:
        model = ShoppingItem
        fields = (
            # Attributes
            'name',
            'image',
            'price',

            # Foreign Key
            'user',
        )
