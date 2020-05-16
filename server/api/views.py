from rest_framework_json_api.views import ModelViewSet
from server.models import ShoppingList, ShoppingItem
from server.api.serializers import ShoppingListSerializer, ShoppingItemSerializer


class ShoppingListViewSet(ModelViewSet):
    """Gives us the api viewset for a shopping list"""
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    class Meta:
        model = ShoppingList


class ShoppingItemViewSet(ModelViewSet):
    """Gives us the api viewset for a shopping item"""
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

    class Meta:
        model = ShoppingItem
