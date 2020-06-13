from rest_framework_json_api import serializers
from server.models import ShoppingItem
from drf_extra_fields.fields import HybridImageField

class ShoppingItemSerializer(serializers.ModelSerializer):
    included_serializers = {
        'user': 'accounts.api.serializers.UserSerializer',
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


class AddShoppingItemSerializer(serializers.ModelSerializer):
    included_serializers = {
        'user': 'accounts.api.serializers.UserSerializer',
    }

    # This field allows the receipt of a bit stream from Android
    image = HybridImageField()

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
