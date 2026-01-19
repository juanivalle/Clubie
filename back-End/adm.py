"""
Script de Administración de Clubie
===================================
Este script permite a los administradores crear cuentas para clubs.
Los clubs se contactan con nosotros y nosotros les generamos sus credenciales.

Uso:
    python adm.py crear         # Crear cuenta con credenciales aleatorias
    python adm.py crear usuario password email  # Crear con datos específicos
    python adm.py listar        # Listar todas las cuentas
"""
import sys
import random
import string

# Configurar path para importar desde el directorio actual
sys.path.insert(0, '.')

from clases import db, Club, app

def generar_username(longitud=8):
    """Genera un nombre de usuario aleatorio"""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_password(longitud=10):
    """Genera una contraseña aleatoria segura"""
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def crear_cuenta(username=None, password=None, email=None):
    """Crea una nueva cuenta de club"""
    with app.app_context():
        # Generar credenciales si no se proporcionan
        if not username:
            username = generar_username()
        if not password:
            password = generar_password()
        if not email:
            email = f"{username.lower()}@club.com"
        
        # Verificar si ya existe
        existente = Club.query.filter_by(username=username).first()
        if existente:
            print(f"\n❌ Error: El usuario '{username}' ya existe.")
            return None
        
        existente_email = Club.query.filter_by(email=email).first()
        if existente_email:
            print(f"\n❌ Error: El email '{email}' ya está registrado.")
            return None
        
        # Crear el club
        nuevo_club = Club(username=username, email=email)
        nuevo_club.set_password(password)
        
        db.session.add(nuevo_club)
        db.session.commit()
        
        print("\n" + "="*50)
        print("✅ CUENTA CREADA EXITOSAMENTE")
        print("="*50)
        print(f"   👤 Usuario:    {username}")
        print(f"   🔑 Contraseña: {password}")
        print(f"   📧 Email:      {email}")
        print("="*50)
        print("\n⚠️  Guarda estas credenciales, la contraseña no se puede recuperar.")
        print()
        
        return {'username': username, 'password': password, 'email': email}

def listar_cuentas():
    """Lista todas las cuentas de clubs registradas"""
    with app.app_context():
        clubs = Club.query.all()
        
        if not clubs:
            print("\n📋 No hay cuentas registradas.")
            return
        
        print("\n" + "="*60)
        print("📋 CUENTAS REGISTRADAS")
        print("="*60)
        print(f"{'ID':<5} {'Usuario':<20} {'Email':<30}")
        print("-"*60)
        
        for club in clubs:
            print(f"{club.id:<5} {club.username:<20} {club.email:<30}")
        
        print("="*60)
        print(f"Total: {len(clubs)} cuenta(s)")
        print()

def mostrar_ayuda():
    """Muestra la ayuda del script"""
    print(__doc__)
    print("Comandos disponibles:")
    print("  crear                        - Crear cuenta con credenciales aleatorias")
    print("  crear <user> <pass> <email>  - Crear cuenta con datos específicos")
    print("  listar                       - Listar todas las cuentas")
    print("  ayuda                        - Mostrar esta ayuda")
    print()

def main():
    if len(sys.argv) < 2:
        mostrar_ayuda()
        return
    
    comando = sys.argv[1].lower()
    
    if comando == 'crear':
        if len(sys.argv) == 2:
            # Crear con credenciales aleatorias
            crear_cuenta()
        elif len(sys.argv) == 5:
            # Crear con credenciales específicas
            crear_cuenta(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("❌ Uso: python adm.py crear [usuario password email]")
    
    elif comando == 'listar':
        listar_cuentas()
    
    elif comando == 'ayuda' or comando == 'help' or comando == '-h':
        mostrar_ayuda()
    
    else:
        print(f"❌ Comando desconocido: {comando}")
        mostrar_ayuda()

if __name__ == '__main__':
    main()