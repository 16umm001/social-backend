from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from social.base.apis import MultipleSerializerMixins
from social.users.serializers import UserCreateSerializer, UserAuthSerializer, UserLoginSerializer, EmptySerializer, \
    PasswordChangeSerializer
from social.users.services import authenticate_user


class UserAuthViewSet(MultipleSerializerMixins, viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    retrieve_auth_serializer = UserAuthSerializer
    serializer_classes = {
        "register": UserCreateSerializer,
        "login": UserLoginSerializer,
        "logout": EmptySerializer,
        "change_password": PasswordChangeSerializer
    }

    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save(is_verified=True)
        response_serializer = self.retrieve_auth_serializer(user, context=self.get_serializer_context())
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate_user(**serializer.validated_data)
        response_data = self.retrieve_auth_serializer(user).data
        return Response(response_data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, url_path="logout", permission_classes=[IsAuthenticated])
    def logout(self, request, *args, **kwargs):
        request._auth.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated], url_path="change-password")
    def change_password(self, request, *args, **kwargs):
        current_user = request.user
        serializer = self.get_serializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        current_user.set_password(serializer.validated_data['new_password'])
        current_user.save()
        return Response({"success": True}, status=status.HTTP_200_OK)
