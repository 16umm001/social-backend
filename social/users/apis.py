from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from social.users.serializers import UserCreateSerializer, UserAuthSerializer


class UserAuthViewSet(viewsets.GenericViewSet):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny, ]
    retrieve_auth_serializer = UserAuthSerializer

    @action(methods=['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save(is_verified=True)
        response_serializer = self.retrieve_auth_serializer(user, context=self.get_serializer_context())
        return HttpResponse(response_serializer.data)
