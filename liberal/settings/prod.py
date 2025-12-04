from .base import *
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ========= CONFIG PROD =========
DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# ========= DATABASE (Render Postgres) =========
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("ERROR: DATABASE_URL no está definida. Render no creó la variable.")

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=True
    )
}

# ========= WHITENOISE =========
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.child("staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ========= CLOUDINARY =========
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# Configurar SDK de Cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)


# TODOS los archivos van a Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# ========= CKEDITOR =========
# Ruta donde CKEditor guarda los archivos
CKEDITOR_UPLOAD_PATH = "uploads/"

# ========= MEDIA (para producción también) =========
#MEDIA_URL = "/media/"
#MEDIA_ROOT = BASE_DIR.child("media")

# ========= CSRF =========
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS if host != "*"
]
