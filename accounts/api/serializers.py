from rest_framework_json_api import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # Attributes
            'username',
            'email',
        )
