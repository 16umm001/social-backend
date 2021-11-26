from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_superuser, is_staff, username, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, username, **extra_field):
        return self._create_user(email, password, False, False, username, **extra_field)

    def create_superuser(self, email, password, username, **extra_field):
        return self._create_user(email, password, True, True, username, **extra_field)
