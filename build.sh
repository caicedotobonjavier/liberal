#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Verificar DATABASE_URL
echo "DATABASE_URL: $DATABASE_URL"

# Listar migraciones
python manage.py showmigrations

# Ejecutar migraciones
python manage.py migrate

# Crear superuser si no existe (opcional)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell || true

python manage.py collectstatic --noinput