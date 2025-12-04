import os
import dj_database_url

from .base import *

# Debug
DEBUG = False

# Secret Key desde variable de entorno
SECRET_KEY = os.environ.get('SECRET_KEY')

# Hosts permitidos
ALLOWED_HOSTS = [
    'liberal-app.onrender.com',  # Tu dominio en Render
    'tu-dominio.com',            # Si tienes dominio personalizado
]

# Base de datos PostgreSQL para Render
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')