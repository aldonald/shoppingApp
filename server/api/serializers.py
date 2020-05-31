from rest_framework_json_api import serializers
from server.models import ShoppingItem
from drf_extra_fields.fields import Base64ImageField

class ShoppingItemSerializer(serializers.ModelSerializer):
    included_serializers = {
        'user': 'accounts.api.serializers.UserSerializer',
    }

    image = Base64ImageField()

    def create(self, validated_data):
        image = validated_data.pop('image')
        name = validated_data.pop('name')
        price = validated_data.pop('price')
        user = self.request.user
        return ShoppingItem.objects.create(name=name, image=image, price=price, user=user)
        
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

