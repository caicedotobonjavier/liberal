"""
WSGI config for liberal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

#import os
#
#from django.core.wsgi import get_wsgi_application
#
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liberal.settings.local')
#
#application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application

# Usa variable de entorno o local por defecto
settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', 'liberal.settings.local')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()