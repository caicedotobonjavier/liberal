import os
import dj_database_url
from .base import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary_storage.storage import MediaCloudinaryStorage

# ==================== DEBUG ====================
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ==================== ALLOWED HOSTS ====================
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'liberal-58ne.onrender.com',
]

# Agregar host dinámico de Render
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# ==================== DATABASE ====================
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# ==================== STATIC FILES ====================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child('staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# ==================== CLOUDINARY CONFIGURATION ====================
print("=" * 50)
print("🔍 VERIFICANDO CLOUDINARY EN PRODUCCIÓN")
print(f"CLOUDINARY_CLOUD_NAME: {os.environ.get('CLOUDINARY_CLOUD_NAME', 'NO SET')}")
print(f"CLOUDINARY_API_KEY: {'SET' if os.environ.get('CLOUDINARY_API_KEY') else 'NO SET'}")
print(f"CLOUDINARY_API_SECRET: {'SET' if os.environ.get('CLOUDINARY_API_SECRET') else 'NO SET'}")
print("=" * 50)

# Verificar que todas las variables existan
CLOUDINARY_CONFIGURED = all([
    os.environ.get('CLOUDINARY_CLOUD_NAME'),
    os.environ.get('CLOUDINARY_API_KEY'),
    os.environ.get('CLOUDINARY_API_SECRET')
])

if CLOUDINARY_CONFIGURED:
    print("✅ TODAS LAS VARIABLES CLOUDINARY CONFIGURADAS")
    
    # 1. Configurar Cloudinary SDK
    cloudinary.config(
        cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key=os.environ.get('CLOUDINARY_API_KEY'),
        api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
        secure=True
    )
    
    # 2. Configurar Django Cloudinary Storage
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
        'SECURE': True,
    }
    
    # 3. FORZAR Cloudinary para todas las imágenes
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    
    # 4. Configurar MEDIA_URL para que Django genere URLs correctas
    MEDIA_URL = '/media/'  # IMPORTANTE: No vacío!
    
    print("✅ CLOUDINARY ACTIVADO CORRECTAMENTE")
    print(f"DEFAULT_FILE_STORAGE: {DEFAULT_FILE_STORAGE}")
    print(f"MEDIA_URL: {MEDIA_URL}")
    
    # Prueba rápida de Cloudinary
    try:
        # Subir una imagen de prueba
        test_result = cloudinary.uploader.upload(
            'https://res.cloudinary.com/demo/image/upload/sample.jpg',
            public_id='test_render',
            folder='test/'
        )
        print(f"✅ Cloudinary funciona: {test_result['secure_url']}")
    except Exception as e:
        print(f"⚠️  Prueba Cloudinary falló: {e}")
else:
    print("⚠️  Cloudinary NO configurado - usando almacenamiento local")
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR.child('media')

# ==================== CKEDITOR CONFIGURATION ====================
# Configurar CKEDITOR para usar Cloudinary en producción
if 'cloudinary_storage' in INSTALLED_APPS and CLOUDINARY_CONFIGURED:
    try:
        CKEDITOR_CONFIGS['default']['filebrowserUploadUrl'] = '/ckeditor/upload/'
        CKEDITOR_CONFIGS['default']['filebrowserBrowseUrl'] = '/ckeditor/browse/'
        print("✅ CKEditor configurado para Cloudinary")
    except Exception as e:
        print(f"⚠️  CKEditor no pudo configurarse: {e}")

# ==================== SEGURIDAD ====================
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    print("✅ Configuración de seguridad activada")