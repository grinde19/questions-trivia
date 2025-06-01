#!/bin/sh

echo "🚀 Iniciando aplicación Flask..."

if [ "$SKIP_MIGRATIONS" != "true" ]; then
  echo "Esperando conexión a la base de datos..."
  sleep 5

  if [ ! -d "migrations" ]; then
    echo "Inicializando sistema de migraciones"
    flask db init
    echo "Creando migración inicial..."
    flask db migrate -m "Initial migration"
    echo "Aplicando migraciones..."
    flask db upgrade
  else
    echo "Migraciones ya existen, aplicando cambios..."
    flask db migrate -m "Auto migration" || true
    flask db upgrade || true
  fi
else
  echo "Saltando migraciones (SKIP_MIGRATIONS=true)"
fi

echo "Aplicación lista en http://localhost:5000"

exec python run.py
