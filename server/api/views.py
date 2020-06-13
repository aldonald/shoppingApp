from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_json_api.views import ModelViewSet
from accounts.models import AccountToken
from django.shortcuts import get_object_or_404
from server.models import ShoppingItem
from server.api.serializers import ShoppingItemSerializer, AddShoppingItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, reverse
from server.app_messaging import send_notification
import logging


# Standard api endpoint for shopping items
class ShoppingItemViewSet(ModelViewSet):
    """Gives us the api viewset for a shopping item"""
    authentication_classes = [
        TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = ShoppingItemSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ShoppingItem.objects.all()
        return ShoppingItem.objects.filter(user=user)

    def delete(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        item = serializer.save()
        item.user = self.request.user
        item.save()
        return item

    class Meta:
        model = ShoppingItem


# This endpoint is specific to adding new shopping items from the app
class AddShoppingItemViewSet(ModelViewSet):
    """Gives us the api viewset for posting a new shopping item"""
    authentication_classes = [
        TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = AddShoppingItemSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ShoppingItem.objects.all()
        return ShoppingItem.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        return redirect('/api/shoppingitems')

    def list(self, request, *args, **kwargs):
        return redirect('/api/shoppingitems')

    def perform_create(self, serializer):
        item = serializer.save()
        item.user = self.request.user
        item.save()
        return item

    class Meta:
        model = ShoppingItem


# View to add item from a Raspberry Pi - API endpoint
class AddItemFromPi(ModelViewSet):
    """Allows items to be added from the Raspberry Pi"""
    authentication_classes = [
        TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = ShoppingItemSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ShoppingItem.objects.all()
        return ShoppingItem.objects.filter(user=user)

    def perform_create(self, serializer):
        item = serializer.save()
        item.user = self.request.user
        item.save()
        user_id = f"{item.user.id}"
        send_notification([user_id], item.name)
        return item

    def delete(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    class Meta:
        model = ShoppingItem
