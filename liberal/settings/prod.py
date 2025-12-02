from .base import *
import os
import dj_database_url

# ========= CONFIG PROD =========
DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# ========= DATABASE (Render Postgres / SQLite fallback) =========
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    # Render con Postgres
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # Si no existe DATABASE_URL → usar SQLite (ideal para pruebas o Render free)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# ========= WHITENOISE =========
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.child("staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ========= CSRF =========
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS if host != "*"
]
