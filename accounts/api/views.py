from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_json_api import serializers
from rest_framework_json_api.views import ModelViewSet
from accounts.models import User, AccountToken
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from accounts.api.serializers import UserSerializer, CreateUserSerializer, CreateAccountTokenSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.core.exceptions import ValidationError


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

        ser_user = UserSerializer(user).data
        return Response(ser_user, status=status.HTTP_201_CREATED)


class AccountTokenView(ModelViewSet):
    """Allows end point to create firebase token"""
    permission_classes = (IsAuthenticated,)
    queryset = AccountToken.objects.all()
    serializer_class = CreateAccountTokenSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = serializer.data
        else:
            try:
                firebaseToken = request.data['firebaseToken']
                AccountToken.objects.get(firebaseToken=firebaseToken)
                data = {'firebaseToken': "Token already exists"}
                headers = {}
            except AccountToken.DoesNotExist:
                serializer.is_valid(raise_exception=True)
        
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            item = serializer.save()
            item.user = self.request.user
            item.save()
        except:
            pass
        return item

    class Meta:
        model = AccountToken
