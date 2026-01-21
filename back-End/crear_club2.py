"""Script para crear clubs de prueba"""
from app import app, db
from clases import Club

with app.app_context():
    # Crear segundo club de prueba
    club2 = Club.query.filter_by(username='club2').first()
    if not club2:
        club2 = Club(username='club2', email='club2@test.com')
        club2.set_password('123456')
        db.session.add(club2)
        db.session.commit()
        print("="*40)
        print("Club 2 creado exitosamente!")
        print("="*40)
        print(f"Usuario: club2")
        print(f"Password: 123456")
        print("="*40)
    else:
        print("Club 2 ya existe")
