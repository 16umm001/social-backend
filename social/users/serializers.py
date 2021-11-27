from collections import defaultdict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from social.users.models import User
from social.users.services import get_user_auth_token, create_user_account, is_username_exists


class AuthTokenMixin(serializers.Serializer):
    auth_token = serializers.SerializerMethodField()

    def get_auth_token(self, obj):
        token = get_user_auth_token(obj)
        return token


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password']
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def validate(self, attrs):
        validation_errors = defaultdict(list)
        password = attrs.get('password')
        username = attrs.get('username')
        if is_username_exists(username):
            validation_errors['username exits'].append('please choose different username')
        if len(password)<8:
            validation_errors['Weak Password'].append('minimum length of password should be 8')
        if validation_errors:
            raise ValidationError(validation_errors)

        return super(UserCreateSerializer, self).validate(attrs)

    def create(self, validated_data):
        user = create_user_account(**validated_data)
        return user


class UserAuthSerializer(AuthTokenMixin, UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ['auth_token']
