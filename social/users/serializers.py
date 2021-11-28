from collections import defaultdict

from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from social.users.models import User
from social.users.services import get_user_auth_token, create_user_account, is_username_exists


class AuthTokenMixin(serializers.Serializer):
    auth_token = serializers.SerializerMethodField()

    def get_auth_token(self, obj):
        token = get_user_auth_token(obj)
        return token

class EmptySerializer(serializers.Serializer):
    pass

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


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = User.objects.filter(email=email).first()
        if not user:
            raise ValidationError("Email does not exists.")
        if user and not user.check_password(password):
            raise ValidationError("Incorrect password")
        return super(UserLoginSerializer, self).validate(attrs)


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise ValidationError("Current password does not match")

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value
