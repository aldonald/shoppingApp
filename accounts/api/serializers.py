from rest_framework_json_api import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # Attributes
            'id',
            'username',
            'email',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # Attributes
            'id',
            'username',
            'email',
            'pasword',
        )
