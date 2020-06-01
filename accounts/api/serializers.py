from rest_framework_json_api import serializers
from accounts.models import User, AccountToken


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
            'password',
        )


class CreateAccountTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountToken
        fields = (
            'token',
        )
