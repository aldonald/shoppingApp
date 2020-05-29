from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_json_api.views import ModelViewSet
from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from accounts.api.serializers import UserSerializer
from rest_framework import status


class IsSuperUser(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class UserViewSet(ModelViewSet):
    """Gives the api viewset for users"""
    permission_classes = [IsSuperUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        if request.user and request.user.is_superuser:
            return super().list(*args, **kwargs)

    def delete(self, request, pk):
        if request.user and request.user.is_superuser:
            item = get_object_or_404(self.queryset, pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
