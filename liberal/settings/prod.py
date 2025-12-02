from .base import *

import os
import dj_database_url

# ========= SECRET KEY =========
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")

# ========= DEBUG =========
DEBUG = False

# ========= ALLOWED HOSTS =========
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# ========= DATABASE =========
DATABASES = {
    "default": dj_database_url.parse(
        os.environ["DATABASE_URL"],
        conn_max_age=600,
        ssl_require=True
    )
}

# ========= STATIC / WHITENOISE =========
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# ========= OTRAS CONFIGS =========
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS if host != "*"
]