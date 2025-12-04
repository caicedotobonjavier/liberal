#!/usr/bin/env bash
set -o errexit
set -x  # Modo verbose para ver cada comando

echo "=== INICIANDO BUILD ==="
echo "Directorio actual: $(pwd)"

# Instalar dependencias
pip install -r requirements.txt

# Verificar Cloudinary
echo "=== VERIFICANDO CLOUDINARY ==="
python -c "
import os
print('Cloudinary variables:')
print(f'CLOUD_NAME: {os.environ.get(\"CLOUDINARY_CLOUD_NAME\")}')
print(f'API_KEY: {os.environ.get(\"CLOUDINARY_API_KEY\")[:5] if os.environ.get(\"CLOUDINARY_API_KEY\") else \"NO\"}...')
print(f'API_SECRET: {os.environ.get(\"CLOUDINARY_API_SECRET\")[:5] if os.environ.get(\"CLOUDINARY_API_SECRET\") else \"NO\"}...')
"

# Ejecutar migraciones
echo "=== APLICANDO MIGRACIONES ==="
python manage.py migrate

# Crear superusuario si no existe
echo "=== CREANDO SUPERUSUARIO ==="
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'Admin123')" | python manage.py shell || true

# Colectar archivos estáticos
echo "=== COLECTANDO STATIC FILES ==="
python manage.py collectstatic --noinput

echo "=== BUILD COMPLETADO ==="