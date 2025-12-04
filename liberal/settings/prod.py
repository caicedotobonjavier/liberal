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


# ========= CLOUDINARY CON VERIFICACIÓN =========
print("🔍 VERIFICANDO CLOUDINARY...")

cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME')
api_key = os.environ.get('CLOUDINARY_API_KEY')
api_secret = os.environ.get('CLOUDINARY_API_SECRET')

print(f"CLOUD_NAME: {cloud_name}")
print(f"API_KEY: {'✅' if api_key else '❌'}")
print(f"API_SECRET: {'✅' if api_secret else '❌'}")

# SOLO si las 3 variables existen
if cloud_name and api_key and api_secret:
    print("✅ TODAS las variables cargadas - Configurando Cloudinary")
    
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': cloud_name,
        'API_KEY': api_key,
        'API_SECRET': api_secret,
    }
    
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )
    
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    MEDIA_URL = "/"
    #MEDIA_URL = "/media/"
    
else:
    print("❌ FALTAN variables de Cloudinary")
    print("⚠️  Usando almacenamiento LOCAL (no persistente en Render)")
    
    CLOUDINARY_STORAGE = {}
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# ========= CONFIGURAR CKEDITOR PARA CLOUDINARY =========
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "cloudinary"  # ¡ESTO FALTA!


# ========= WHITENOISE =========
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.child("staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ========= CKEDITOR =========
# Ruta donde CKEditor guarda los archivos
#CKEDITOR_UPLOAD_PATH = "uploads/"

# ========= MEDIA (para producción también) =========

#MEDIA_ROOT = BASE_DIR.child("media")

# ========= CSRF =========
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS if host != "*"
]


# ========= FINAL CHECK =========
print(f"✅ Configuración finalizada")
print(f"   DEFAULT_FILE_STORAGE: {DEFAULT_FILE_STORAGE}")