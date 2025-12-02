from .base import *
import os
import dj_database_url

# ========= CONFIG PROD =========
DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# ========= DATABASE (Render Postgres) =========
DATABASES = {
    "default": dj_database_url.parse(
        os.environ["DATABASE_URL"],
        conn_max_age=600,
        ssl_require=True
    )
}

# ========= WHITENOISE =========
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.child("staticfiles")

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# ========= CSRF =========
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS if host != "*"
]
