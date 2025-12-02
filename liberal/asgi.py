#"""
#ASGI config for liberal project.
#
#It exposes the ASGI callable as a module-level variable named ``application``.
#
#For more information on this file, see
#https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
#"""
#
#import os
#
#from django.core.asgi import get_asgi_application
#
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liberal.settings.local')
#
#application = get_asgi_application()


"""
ASGI config for liberal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Usar prod por defecto, a menos que DJANGO_SETTINGS_MODULE exista
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'liberal.settings.prod'   # archivo prod.py
)

application = get_asgi_application()
