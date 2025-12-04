#from django.core.exceptions import ImproperlyConfigured
#import json
#
## Build paths inside the project like this: BASE_DIR / 'subdir'.
#from unipath import Path
#BASE_DIR = Path(__file__).resolve().ancestor(3)
#
## Quick-start development settings - unsuitable for production
## See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
#
## SECURITY WARNING: keep the secret key used in production secret!
#with open("secret.json") as f:
#    secret = json.loads(f.read())
#
#def get_secret(secrest_name, secrets=secret):
#    try:
#        return secrets[secrest_name]
#    except:
#        msg = "la variable no %s existe" %secrest_name
#        raise ImproperlyConfigured(msg)
#    
#SECRET_KEY = get_secret('SECRET_KEY')
#
#
#
## Application definition
#
#DJANGO_APPS = (
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#)
#
#THIRD_PARTY_APPS = (
#    'ckeditor',
#    'ckeditor_uploader',
#)
#
#LOCAL_APPS = (
#    'applications.users',
#    'applications.municipios',
#    'applications.visitas',
#    'applications.home',
#    'applications.eventos',
#    'applications.contacto',
#    'applications.equipo',
#)
#
#
#INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
#
#MIDDLEWARE = [
#    'django.middleware.security.SecurityMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#]
#
#ROOT_URLCONF = 'liberal.urls'
#
#TEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'DIRS': [BASE_DIR.child('templates')],
#        'APP_DIRS': True,
#        'OPTIONS': {
#            'context_processors': [
#                'django.template.context_processors.request',
#                'django.contrib.auth.context_processors.auth',
#                'django.contrib.messages.context_processors.messages',
#            ],
#        },
#    },
#]
#
#WSGI_APPLICATION = 'liberal.wsgi.application'
#
#
## Password validation
## https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
#
#AUTH_PASSWORD_VALIDATORS = [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
#]
#
#
## Internationalization
## https://docs.djangoproject.com/en/5.2/topics/i18n/
#
#LANGUAGE_CODE = 'es-ES'
#
#TIME_ZONE = 'UTC'
#
#USE_I18N = True
#
#USE_TZ = True
#
## Default primary key field type
## https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
#
#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
#
#AUTH_USER_MODEL = 'users.USER'



from django.core.exceptions import ImproperlyConfigured
import json
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from unipath import Path
BASE_DIR = Path(__file__).resolve().ancestor(3)

# SECURITY WARNING: keep the secret key used in production secret!
def get_secret(secret_name):
    """Obtiene secretos de secret.json o variables de entorno"""
    # 1. Intentar desde archivo secret.json (desarrollo local)
    try:
        with open("secret.json") as f:
            secret = json.loads(f.read())
            return secret[secret_name]
    except FileNotFoundError:
        pass
    
    # 2. Intentar desde variable de entorno (Render/producción)
    env_value = os.environ.get(secret_name)
    if env_value:
        return env_value
    
    # 3. Si no se encuentra, error
    msg = f"La variable {secret_name} no existe"
    raise ImproperlyConfigured(msg)

SECRET_KEY = get_secret('SECRET_KEY')

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'ckeditor',
    'ckeditor_uploader',
    'cloudinary',           # AÑADIDO
    'cloudinary_storage',   # AÑADIDO
)

LOCAL_APPS = (
    'applications.users',
    'applications.municipios',
    'applications.visitas',
    'applications.home',
    'applications.eventos',
    'applications.contacto',
    'applications.equipo',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'liberal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'liberal.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'es-ES'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.USER'

# Configuración CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

# ==================== STATIC & MEDIA FILES (DESARROLLO) ====================
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

# Media files (uploaded by users) - CONFIGURACIÓN LOCAL
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

print("=" * 50)
print("BASE SETTINGS LOADED - MODO DESARROLLO")
print(f"MEDIA_URL: {MEDIA_URL}")
print(f"DEFAULT_FILE_STORAGE: {DEFAULT_FILE_STORAGE}")
print("=" * 50)