"""
Script para agregar datos de cosecha de prueba
"""
import sys
sys.path.insert(0, '.')

from datetime import datetime, timedelta
from clases import db, Trazabilidad, app

RAZAS_COSECHA = [
    ('OG Kush', 150),
    ('Blue Dream', 200),
    ('White Widow', 120),
    ('Amnesia Haze', 80),
    ('Critical Kush', 250),
]

with app.app_context():
    print('='*50)
    print('Agregando datos de cosecha...')
    print('='*50)
    
    for raza, cantidad in RAZAS_COSECHA:
        # Buscar si ya existe una planta con esta raza
        planta = Trazabilidad.query.filter_by(raza=raza).first()
        
        if planta:
            # Actualizar con fecha de cosecha
            planta.cosecha = datetime.now() - timedelta(days=30)
            planta.cantidad = str(cantidad)
            print(f"  ✅ Actualizado: {raza} - {cantidad}g cosechados")
        else:
            # Crear nueva planta con cosecha
            nueva_planta = Trazabilidad(
                raza=raza,
                cantidad=str(cantidad),
                Enraizado=datetime.now() - timedelta(days=120),
                floracion=datetime.now() - timedelta(days=60),
                cosecha=datetime.now() - timedelta(days=30),
                observaciones='Planta con cosecha'
            )
            db.session.add(nueva_planta)
            print(f"  ✅ Creado: {raza} - {cantidad}g cosechados")
    
    db.session.commit()
    
    # Mostrar estado final
    print('\n' + '='*50)
    print('Estado actual del catálogo:')
    print('='*50)
    
    plantas_cosechadas = Trazabilidad.query.filter(Trazabilidad.cosecha.isnot(None)).all()
    for p in plantas_cosechadas:
        print(f"  🌿 {p.raza}: {p.cantidad}g")
    
    print('='*50)
    print('✅ Datos de cosecha agregados!')
    print('='*50)
