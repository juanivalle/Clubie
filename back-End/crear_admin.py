"""
Script para crear usuario admin en Clubie
Ejecutar con: python crear_admin.py
"""
import sys
sys.path.insert(0, '.')

from clases import db, Club, app

with app.app_context():
    # Crear todas las tablas
    db.create_all()
    
    # Verificar si el usuario admin ya existe
    existing = Club.query.filter_by(username='admin').first()
    if existing:
        print('El usuario admin ya existe!')
    else:
        # Crear usuario admin
        admin = Club(username='admin', email='admin@club.com')
        admin.set_password('123456')
        db.session.add(admin)
        db.session.commit()
        print('='*40)
        print('Usuario admin creado exitosamente!')
        print('='*40)
        print('Usuario: admin')
        print('Password: 123456')
        print('='*40)
