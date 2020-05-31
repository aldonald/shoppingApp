from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_json_api.views import ModelViewSet
from django.shortcuts import get_object_or_404
from server.models import ShoppingItem
from server.api.serializers import ShoppingItemSerializer
from rest_framework.response import Response
from rest_framework import status
import logging


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

    # def perform_create(self, serializer):
    #     import base64
    #     import pdb; pdb.set_trace()
    #     data = serializer.data['image']
    #     format, imgstr = data.split(';base64,')
    #     ext = format.split('/')[-1]
    #     data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    #     logging.error(serializer.data)
    #     item = serializer.save()
    #     item.user = self.request.user
    #     item.save()
    #     return item

    def post(self, request, *args, **kwargs):
        serializer = ShoppingItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    class Meta:
        model = ShoppingItem
