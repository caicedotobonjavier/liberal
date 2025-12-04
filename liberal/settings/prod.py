import os
import dj_database_url
from .base import *

# Debug
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Debug info
print("=" * 50)
print("PRODUCTION SETTINGS LOADED")
print(f"DEBUG: {DEBUG}")
print(f"DATABASE_URL: {'CONFIGURADO' if os.environ.get('DATABASE_URL') else 'NO CONFIGURADO'}")
print("=" * 50)

# Hosts permitidos
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# Agregar host dinámico de Render
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    print(f"RENDER_EXTERNAL_HOSTNAME: {RENDER_EXTERNAL_HOSTNAME}")

# Agregar tu dominio de Render actual
ALLOWED_HOSTS.append('liberal-58ne.onrender.com')

# Base de datos PostgreSQL para Render
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Static files para producción
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child('staticfiles')

# WhiteNoise para servir archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# En producción, CKEDITOR debe usar Cloudinary si está configurado
if 'cloudinary_storage' in INSTALLED_APPS:
    try:
        # Configurar CKEDITOR para usar Cloudinary
        CKEDITOR_CONFIGS['default']['filebrowserUploadUrl'] = '/ckeditor/upload/'
        CKEDITOR_CONFIGS['default']['filebrowserBrowseUrl'] = '/ckeditor/browse/'
    except:
        pass

# Seguridad en producción (solo si DEBUG=False)
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    print("✅ Configuración de seguridad activada")


# ==================== FORZAR CLOUDINARY EN PRODUCCIÓN ====================
import os

# Verificar variables Cloudinary en producción
CLOUDINARY_ENV_VARS = all([
    os.environ.get('CLOUDINARY_CLOUD_NAME'),
    os.environ.get('CLOUDINARY_API_KEY'),
    os.environ.get('CLOUDINARY_API_SECRET')
])

if CLOUDINARY_ENV_VARS and 'cloudinary_storage' in INSTALLED_APPS:
    # SOBREESCRIBIR configuración de base.py
    print("=== FORZANDO CLOUDINARY EN PRODUCCIÓN ===")
    
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    }
    
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    MEDIA_URL = ''
    
    # Importar y configurar Cloudinary SDK
    import cloudinary
    cloudinary.config(
        cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key=os.environ.get('CLOUDINARY_API_KEY'),
        api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
        secure=True
    )
    
    print("✅ CLOUDINARY FORZADO EN PRODUCCIÓN")
else:
    print("⚠️  Cloudinary no forzado - variables faltantes")
# ==================== FIN FORZAR CLOUDINARY ====================