#"""
#WSGI config for liberal project.
#
#It exposes the WSGI callable as a module-level variable named ``application``.
#
#For more information on this file, see
#https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
#"""
#
#import os
#
#from django.core.wsgi import get_wsgi_application
#
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liberal.settings.local')
#
#application = get_wsgi_application()


"""
WSGI config for liberal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Si DJANGO_SETTINGS_MODULE no está definido, usar prod como fallback
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'liberal.settings.prod'   # nombre correcto del archivo prod.py
)

application = get_wsgi_application()
