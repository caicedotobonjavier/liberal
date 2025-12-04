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