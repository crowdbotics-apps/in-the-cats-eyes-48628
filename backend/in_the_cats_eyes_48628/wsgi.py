"""
WSGI config for in_the_cats_eyes_48628 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "in_the_cats_eyes_48628.settings"
)

application = get_wsgi_application()
