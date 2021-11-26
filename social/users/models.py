from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    phone_number = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=128)

    def __str__(self):
        return self.email
