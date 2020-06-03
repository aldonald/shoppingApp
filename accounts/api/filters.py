from django_filters import rest_framework as filters
from accounts.models import User


class UserFilterSet(filters.FilterSet):
    username = filters.CharFilter(field_name='username')
    id = filters.CharFilter(field_name='id')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]
