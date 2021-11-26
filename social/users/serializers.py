from rest_framework import serializers

from social.users.models import User
from social.users.services import get_user_auth_token, create_user_account


class AuthTokenMixin(serializers.Serializer):
    auth_token = serializers.SerializerMethodField()

    def get_auth_token(self, obj):
        token = get_user_auth_token(obj)
        return token


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password']

    def create(self, validated_data):
        user = create_user_account(**validated_data)
        return user


class UserAuthSerializer(AuthTokenMixin, UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ['auth_token']
