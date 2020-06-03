from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework_json_api import serializers
from rest_framework_json_api.views import ModelViewSet
from accounts.models import User, AccountToken
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from accounts.api.serializers import UserSerializer, CreateUserSerializer, AccountTokenSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.core.exceptions import ValidationError
import logging
from rest_framework.decorators import action
from pusher_push_notifications import PushNotifications
from django.http import JsonResponse
from accounts.api.filters import UserFilterSet
from rest_framework import filters


beams_client = PushNotifications(
    instance_id='8d9473dd-0a61-4ac4-88de-d5dc18ad095a',
    secret_key='DFF47EC3886A6D1C2947F6A1C3ADD2D91D1256DF73E52A408D247A7A8E8BCA11',
)

class ViewIfAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == 'POST' and request.user.is_authenticated:
            return True
        else:
            return False


class NormalAccessPerm(permissions.BasePermission):
    def has_permission(self, request, view):
        logging.warning(
            f"{request.user} is trying to log in. They are authenticated {request.user.is_authenticated}. They are a superuser: {request.user.is_superuser}.")
        if request.user.is_superuser:
            return True
        elif request.method == 'GET' and request.user.is_authenticated:
            return True
        else:
            return False


class UserViewSet(ModelViewSet):
    """Gives the api viewset for users"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [NormalAccessPerm]
    serializer_class = UserSerializer
    filter_class = UserFilterSet

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(user=user)

    def delete(self, request, pk):
        if request.user and request.user.is_superuser:
            item = get_object_or_404(self.queryset, pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def beams_auth(self, request):
        user = request.user
        tokens = AccountToken.objects.filter(user=user)
        logging.warning(
            f"beams_auth was called. There was a token already: {tokens.exists()}")
        if not tokens.exists():
            beams_token = beams_client.generate_token(user.id)
            new_token = AccountToken(
                firebaseToken=beams_token,
                user=user
            )
            new_token.save()
        else:
            beams_token = tokens.last()
        beams_token = AccountTokenSerializer(beams_token).data
        logging.warning(f"{beams_token} is the token sent")
        return JsonResponse(beams_token)


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


# class AccountTokenView(ModelViewSet):
#     """Allows end point to create firebase token"""
#     authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
#     permission_classes = (ViewIfAdminPermission,)
#     queryset = AccountToken.objects.all()
#     serializer_class = AccountTokenSerializer
#     # http_method_names = ['post']

#     def create(self, request, *args, **kwargs):
#         logging.warning(request.data)
#         serializer = self.get_serializer(data=request.data)
#         logging.warning(serializer)
#         if serializer.is_valid():
#             logging.warning("Serializer valid")
#             self.perform_create(serializer)
#             headers = self.get_success_headers(serializer.data)
#             data = serializer.data
#         else:
#             try:
#                 firebaseToken = request.data['firebaseToken']
#                 logging.warning(f"token is {firebaseToken}")
#                 token = AccountToken.objects.get(firebaseToken=firebaseToken)
#                 if (token): logging.warning(f"token retrieved")
#                 data = {'firebaseToken': "Token already exists"}
#                 headers = {}
#             except AccountToken.DoesNotExist:
#                 logging.warning(f"token did not exist")
#                 serializer.is_valid(raise_exception=True)
        
#         return Response(data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         item = serializer.save()
#         item.user = self.request.user
#         item.save()
#         return item
        

#     class Meta:
#         model = AccountToken
