"""
WSGI config for TIFOSS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from os.path import dirname
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append(dirname(dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TIFOSS.settings")

application = get_wsgi_application()
