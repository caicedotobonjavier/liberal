#!/usr/bin/env bash
set -o errexit
set -x  # Modo verbose para ver cada comando

echo "=== INICIANDO BUILD ==="
echo "Directorio actual: $(pwd)"
echo "DATABASE_URL: $DATABASE_URL"

# Instalar dependencias
pip install -r requirements.txt

# Listar migraciones disponibles
echo "=== MIGRACIONES DISPONIBLES ==="
python manage.py showmigrations

# Ejecutar migraciones
echo "=== APLICANDO MIGRACIONES ==="
python manage.py migrate

# Verificar tablas creadas
echo "=== VERIFICANDO TABLAS ==="
python manage.py dbshell << EOF
\dt
EOF

# Crear superusuario si no existe
echo "=== CREANDO SUPERUSUARIO ==="
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'Admin123')" | python manage.py shell || true

# Colectar archivos estáticos
echo "=== COLECTANDO STATIC FILES ==="
python manage.py collectstatic --noinput

echo "=== BUILD COMPLETADO ==="

# Al final de build.sh
echo "=== PRUEBA DIRECTA CLOUDINARY ==="
python -c "
import cloudinary
import cloudinary.uploader
import os
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    secure=True
)
print('Cloudinary config OK')
# Intenta subir una imagen de prueba
try:
    result = cloudinary.uploader.upload('https://res.cloudinary.com/demo/image/upload/sample.jpg', public_id='test_render')
    print(f'✅ Cloudinary funciona: {result[\"url\"]}')
except Exception as e:
    print(f'❌ Cloudinary error: {e}')
"