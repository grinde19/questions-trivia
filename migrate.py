import os
import sys
from flask_migrate import init, migrate, upgrade
from app import create_app, db

def run_migrations():
    app = create_app()
    
    with app.app_context():
        # Verificar si existe el directorio de migraciones
        migrations_dir = 'migrations'
        
        # Verificar si migrations/ existe Y tiene los archivos necesarios
        env_py_path = os.path.join(migrations_dir, 'env.py')
        
        if not os.path.exists(migrations_dir) or not os.path.exists(env_py_path):
            print("Inicializando migraciones...")
            try:
                # Eliminar carpeta vacía si existe
                if os.path.exists(migrations_dir) and not os.path.exists(env_py_path):
                    import shutil
                    shutil.rmtree(migrations_dir)
                    print("Eliminando carpeta migrations vacía")
                
                init()
                print("Migraciones inicializadas correctamente")
            except Exception as e:
                print(f"Error al inicializar migraciones: {e}")
                return False
        
        # Crear nueva migración
        print("Creando migración...")
        try:
            migrate(message="Initial migration")
            print("Migración creada")
        except Exception as e:
            print(f"Info: {e}")
            # Puede fallar si no hay cambios, continuar
        
        # Aplicar migraciones
        print("Aplicando migraciones...")
        try:
            upgrade()
            print("Migraciones aplicadas correctamente")
            return True
        except Exception as e:
            print(f"Error al aplicar migraciones: {e}")
            return False

if __name__ == '__main__':
    success = run_migrations()
    if not success:
        sys.exit(1)