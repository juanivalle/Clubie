"""Script para crear admin puro y clubs con datos de prueba"""
from app import app, db
from clases import Club, User, Trazabilidad, Ventas
from datetime import datetime, timedelta

with app.app_context():
    # Limpiar base de datos
    db.drop_all()
    db.create_all()
    
    # ============================================
    # 1. Crear ADMIN PURO (solo superusuario)
    # ============================================
    admin = Club(username='admin', email='admin@clubie.com', is_superuser=True)
    admin.set_password('admin123')
    db.session.add(admin)
    
    # ============================================
    # 2. Crear CLUB VERDE
    # ============================================
    club_verde = Club(username='ClubVerde', email='verde@test.com', is_superuser=False)
    club_verde.set_password('verde123')
    db.session.add(club_verde)
    db.session.flush()  # Para obtener el ID
    
    # Miembros del Club Verde
    miembros_verde = [
        User(cedula=11111111, name='Juan Perez', telefono=91234567, email='juan@verde.com', club_id=club_verde.id),
        User(cedula=22222222, name='Maria Garcia', telefono=91234568, email='maria@verde.com', club_id=club_verde.id),
        User(cedula=33333333, name='Carlos Lopez', telefono=91234569, email='carlos@verde.com', club_id=club_verde.id),
    ]
    db.session.add_all(miembros_verde)
    
    # Plantas del Club Verde
    plantas_verde = [
        Trazabilidad(idplanta=1, raza='White Widow', cantidad='150', club_id=club_verde.id,
                     Enraizado=datetime.now()-timedelta(days=90), cosecha=datetime.now()-timedelta(days=5)),
        Trazabilidad(idplanta=2, raza='OG Kush', cantidad='200', club_id=club_verde.id,
                     Enraizado=datetime.now()-timedelta(days=85), cosecha=datetime.now()-timedelta(days=3)),
        Trazabilidad(idplanta=3, raza='Blue Dream', cantidad='100', club_id=club_verde.id,
                     Enraizado=datetime.now()-timedelta(days=60)),  # Sin cosechar
    ]
    db.session.add_all(plantas_verde)
    
    # Ventas del Club Verde
    ventas_verde = [
        Ventas(cedula=11111111, raza='White Widow', cantidad=20, retiro=datetime.now()-timedelta(days=2), club_id=club_verde.id),
        Ventas(cedula=22222222, raza='OG Kush', cantidad=15, retiro=datetime.now()-timedelta(days=1), club_id=club_verde.id),
    ]
    db.session.add_all(ventas_verde)
    
    # ============================================
    # 3. Crear CLUB NATURAL
    # ============================================
    club_natural = Club(username='ClubNatural', email='natural@test.com', is_superuser=False)
    club_natural.set_password('natural123')
    db.session.add(club_natural)
    db.session.flush()
    
    # Miembros del Club Natural
    miembros_natural = [
        User(cedula=44444444, name='Ana Martinez', telefono=98765432, email='ana@natural.com', club_id=club_natural.id),
        User(cedula=55555555, name='Pedro Sanchez', telefono=98765433, email='pedro@natural.com', club_id=club_natural.id),
    ]
    db.session.add_all(miembros_natural)
    
    # Plantas del Club Natural (IDs diferentes porque idplanta es único)
    plantas_natural = [
        Trazabilidad(idplanta=4, raza='Critical Kush', cantidad='250', club_id=club_natural.id,
                     Enraizado=datetime.now()-timedelta(days=100), cosecha=datetime.now()-timedelta(days=10)),
        Trazabilidad(idplanta=5, raza='Amnesia Haze', cantidad='180', club_id=club_natural.id,
                     Enraizado=datetime.now()-timedelta(days=95), cosecha=datetime.now()-timedelta(days=7)),
    ]
    db.session.add_all(plantas_natural)
    
    # Ventas del Club Natural
    ventas_natural = [
        Ventas(cedula=44444444, raza='Critical Kush', cantidad=30, retiro=datetime.now()-timedelta(days=3), club_id=club_natural.id),
    ]
    db.session.add_all(ventas_natural)
    
    db.session.commit()
    
    print("="*50)
    print("BASE DE DATOS CONFIGURADA EXITOSAMENTE")
    print("="*50)
    print()
    print("CUENTAS CREADAS:")
    print("-"*50)
    print("ADMIN (Panel de Administración):")
    print("  Usuario: admin")
    print("  Password: admin123")
    print()
    print("CLUB VERDE:")
    print("  Usuario: ClubVerde")
    print("  Password: verde123")
    print("  Miembros: Juan, Maria, Carlos")
    print("  Razas: White Widow, OG Kush, Blue Dream")
    print()
    print("CLUB NATURAL:")
    print("  Usuario: ClubNatural")
    print("  Password: natural123")
    print("  Miembros: Ana, Pedro")
    print("  Razas: Critical Kush, Amnesia Haze")
    print("="*50)
