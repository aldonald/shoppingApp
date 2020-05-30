from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_json_api import serializers
from rest_framework_json_api.views import ModelViewSet
from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from accounts.api.serializers import UserSerializer, CreateUserSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView


class UserViewSet(ModelViewSet):
    """Gives the api viewset for users"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        if request.user and request.user.is_superuser:
            return super().list(request, *args, **kwargs)

    def delete(self, request, pk):
        if request.user and request.user.is_superuser:
            item = get_object_or_404(self.queryset, pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    class Meta:
        model = User


class CreateUserView(CreateAPIView):
    """Allows end point to create user"""
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        data = CreateUserSerializer(request.data).data
        find_user = User.objects.filter(username=data['username'])
        if not find_user.exists():
            user = User(
                username=data['username'],
                email=data['email']
            )
            user.set_password(data['password'])
            user.save()
        else:
            user = find_user.first()

        ser_user = CreateUserSerializer(user).data
        return Response(ser_user, status=status.HTTP_201_CREATED)
