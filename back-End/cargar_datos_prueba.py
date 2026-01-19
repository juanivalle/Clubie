"""
Script para cargar datos de prueba en Clubie
"""
import sys
sys.path.insert(0, '.')

from datetime import datetime, timedelta
import random
from clases import db, User, Ventas, Trazabilidad, app

# Datos de prueba
RAZAS = ['OG Kush', 'Blue Dream', 'White Widow', 'Amnesia Haze', 'Critical Kush', 
         'Girl Scout Cookies', 'Sour Diesel', 'Purple Haze']

NOMBRES = [
    ('Juan', 'Perez', 'Garcia'),
    ('Maria', 'Lopez', 'Rodriguez'),
    ('Carlos', 'Gonzalez', 'Martinez'),
    ('Ana', 'Fernandez', 'Diaz'),
    ('Pedro', 'Sanchez', 'Ruiz'),
]

with app.app_context():
    print('='*50)
    print('Cargando datos de prueba...')
    print('='*50)
    
    # 1. Crear miembros
    print('\n📋 Creando miembros...')
    miembros_creados = []
    for i, (nombre, apellido1, apellido2) in enumerate(NOMBRES):
        cedula = str(10000000 + i * 1111111)
        nombre_completo = f"{nombre} {apellido1} {apellido2}"
        
        # Verificar si ya existe
        existente = User.query.filter_by(cedula=cedula).first()
        if not existente:
            miembro = User(
                name=nombre_completo,
                cedula=cedula,
                telefono=99000000 + i * 111111,
                email=f"{nombre.lower()}@test.com"
            )
            db.session.add(miembro)
            miembros_creados.append(cedula)
            print(f"   ✅ {nombre_completo} (CI: {cedula})")
        else:
            miembros_creados.append(cedula)
            print(f"   ⏭️  {nombre_completo} ya existe")
    
    db.session.commit()
    
    # 2. Crear ventas con diferentes fechas
    print('\n💰 Creando ventas...')
    ventas_creadas = 0
    
    # Ventas del año actual (2026)
    for mes in range(1, 13):  # Enero a Diciembre
        # 2-4 ventas por mes
        num_ventas = random.randint(2, 4)
        for _ in range(num_ventas):
            dia = random.randint(1, 28)
            fecha = datetime(2026, mes, dia, random.randint(9, 20), random.randint(0, 59))
            
            venta = Ventas(
                cedula=random.choice(miembros_creados),
                raza=random.choice(RAZAS),
                cantidad=random.randint(5, 30),
                retiro=fecha
            )
            db.session.add(venta)
            ventas_creadas += 1
    
    # Algunas ventas del año anterior (2025)
    for mes in range(10, 13):  # Oct-Dic 2025
        num_ventas = random.randint(1, 3)
        for _ in range(num_ventas):
            dia = random.randint(1, 28)
            fecha = datetime(2025, mes, dia, random.randint(9, 20), random.randint(0, 59))
            
            venta = Ventas(
                cedula=random.choice(miembros_creados),
                raza=random.choice(RAZAS),
                cantidad=random.randint(5, 25),
                retiro=fecha
            )
            db.session.add(venta)
            ventas_creadas += 1
    
    db.session.commit()
    print(f"   ✅ {ventas_creadas} ventas creadas")
    
    # 3. Crear algunas plantas
    print('\n🌱 Creando plantas de trazabilidad...')
    plantas_creadas = 0
    for raza in RAZAS[:5]:
        planta = Trazabilidad(
            raza=raza,
            cantidad=str(random.randint(3, 10)),
            Enraizado=datetime(2026, 1, random.randint(1, 15)),
            observaciones='Planta de prueba'
        )
        db.session.add(planta)
        plantas_creadas += 1
        print(f"   ✅ {raza}")
    
    db.session.commit()
    
    print('\n' + '='*50)
    print('✅ DATOS CARGADOS EXITOSAMENTE')
    print('='*50)
    print(f'   👥 Miembros: {len(miembros_creados)}')
    print(f'   💰 Ventas: {ventas_creadas}')
    print(f'   🌱 Plantas: {plantas_creadas}')
    print('='*50)
    print('\n🔑 Credenciales de acceso:')
    print('   Usuario: admin')
    print('   Password: 123456')
    print('='*50)
