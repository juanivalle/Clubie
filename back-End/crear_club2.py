"""Script para crear clubs específicos"""
from app import app, db, generar_password
from clases import Club

with app.app_context():
    cuentas = ['JuanIgnacioValle', 'AgustinMeriles']
    
    for username in cuentas:
        if not Club.query.filter_by(username=username).first():
            # Generar contraseña segura de 12 caractes (mismo estilo que club)
            password = generar_password(12)
            
            # Crear cuenta
            nuevo_club = Club(username=username, email=f'{username.lower()}@clubie.com')
            nuevo_club.set_password(password)
            
            db.session.add(nuevo_club)
            db.session.commit()
            
            print("="*50)
            print(f"✅ Cuenta creada: {username}")
            print(f"🔑 Contraseña:   {password}")
            print("="*50)
        else:
            print(f"ℹ️  La cuenta {username} ya existe")
