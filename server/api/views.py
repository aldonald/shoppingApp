from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_json_api.views import ModelViewSet
from django.shortcuts import get_object_or_404
from server.models import ShoppingList, ShoppingItem
from server.api.serializers import ShoppingListSerializer, ShoppingItemSerializer
from rest_framework.response import Response
from rest_framework import status


class ShoppingListViewSet(ModelViewSet):
    """Gives us the api viewset for a shopping list"""
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    class Meta:
        model = ShoppingList


class ShoppingItemViewSet(ModelViewSet):
    """Gives us the api viewset for a shopping item"""
    authentication_classes = [
        TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

    def delete(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def post(self, request, format = None):
    # if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class Meta:
        model = ShoppingItem
