"""
ASGI config for social project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

import django
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social.settings.local")
django.setup()

application = get_asgi_application()
