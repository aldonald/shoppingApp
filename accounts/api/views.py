from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_json_api.views import ModelViewSet
from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from accounts.api.serializers import UserSerializer, CreateUserSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView


class IsValidUser(IsAuthenticated):
    def get_permissions(self, request, view):
        return request.user and request.user.is_superuser


class UserViewSet(ModelViewSet):
    """Gives the api viewset for users"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsValidUser]
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
    # allowed_methods = ['POST']

    # def get(self, *args, **kwargs):
    #     return None

    # def create(self, request, validated_data, *args, **kwargs):
    #     import pdb; pdb.set_trace()
    #     user = super().create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    class Meta:
        model = User
