from django_filters import rest_framework as filters
from accounts.models import User


# Filters to allow the app to get the user's id - and set up with Beams
class UserFilterSet(filters.FilterSet):
    username = filters.CharFilter(field_name='username')
    id = filters.CharFilter(field_name='id')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]
