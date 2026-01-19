"""
Script para agregar columnas faltantes y crear el superadmin
Este script NO elimina la base de datos, solo agrega lo que falta
"""
import sys
sys.path.insert(0, '.')

from clases import db, Club, app
from sqlalchemy import text

with app.app_context():
    # Intentar agregar las columnas si no existen (SQLite no soporta ALTER bien, pero intentamos)
    try:
        db.session.execute(text('ALTER TABLE club ADD COLUMN is_superuser BOOLEAN DEFAULT 0'))
        print("✅ Columna is_superuser agregada")
    except Exception as e:
        print(f"ℹ️  Columna is_superuser ya existe o error: {e}")
    
    try:
        db.session.execute(text('ALTER TABLE club ADD COLUMN fecha_creacion DATETIME'))
        print("✅ Columna fecha_creacion agregada")
    except Exception as e:
        print(f"ℹ️  Columna fecha_creacion ya existe o error: {e}")
    
    db.session.commit()
    
    # Verificar si ya existe el superadmin
    superadmin = Club.query.filter_by(username='superadmin').first()
    
    if superadmin:
        # Actualizar a superuser si no lo es
        superadmin.is_superuser = True
        db.session.commit()
        print("\n✅ Usuario superadmin ya existía, actualizado a superusuario")
    else:
        # Crear superadmin
        superadmin = Club(
            username='superadmin',
            email='admin@clubie.com',
            is_superuser=True
        )
        superadmin.set_password('Admin123!')
        db.session.add(superadmin)
        db.session.commit()
        print("\n✅ Superadmin creado")
    
    # También marcar la cuenta admin existente si existe
    admin = Club.query.filter_by(username='admin').first()
    if admin:
        admin.is_superuser = True
        db.session.commit()
        print("✅ Cuenta 'admin' también marcada como superusuario")
    
    print("\n" + "="*50)
    print("✅ SUPERADMIN LISTO")
    print("="*50)
    print("   👤 Usuario:    superadmin")
    print("   🔑 Contraseña: Admin123!")
    print("   📧 Email:      admin@clubie.com")
    print("="*50)
    print("\n🔗 Accede a: http://127.0.0.1:5000/login")
    print()
