from django.contrib.auth import get_user_model
from knox.models import AuthToken


def get_user_auth_token(user):
    _, token = AuthToken.objects.create(user)
    return token


def create_user_account(email, password, username, first_name="", last_name="", **extra_field):
    user = get_user_model().objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password, **extra_field)
    return user


def is_username_exists(username):
    is_user_exists = get_user_model().objects.filter(username=username).exists()
    return is_user_exists
