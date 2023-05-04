#!/usr/bin/python3
"""Creation of the diferent clases that we need"""
import uuid4
import re #

class User():
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(30, nullable=False))
    pType = db.Column(db.Integer(1, ))
#CORROBAR INGRSO DE TIPO DE USUARIO, CLIENTE = 1, CLUB = 2
    @app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Cuenta ya existente'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Mail invalido'
        elif not re.match(r'[A-Za-z]+', username):
            msg = 'Usuario con caracteres inválidos'
        elif not username or not password or not email:
            msg = 'Ingreso de datos incorrectos'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'Registrado correctamente'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

  

class Plant():
    """Define the new class Plant"""
    def __init__(self, idRaza, cantidad, riego, sustrato, cortes, Luz, Poda, residuos):
        self.idRaza = idRaza
        self.cantidad = cantidad
        self.riego = riego
        self.sustrato = sustrato
        self.cortes = cortes
        self.luz = Luz
        self.poda = Poda
        self.residuos = residuos

    @property
    def idRaza(self):
        return self.idRaza

    @idRaza.setter
    def idRaza(self, value):
        if not value:
            raise TypeError("Es obligatorio indicar la raza")
        self.idRaza = value

    @property
    def cantidad(self):
        return self.cantidad
    
    @cantidad.setter
    def cantidad(self, value):
        if value <= 0:
            raise ValueError("La cantidad debe ser un número entero y mayor que 0")
        self.cantidad = value

    #SIN TERMINAR

class Cogo():
    """Define the new class Cogo"""
    def __init__(self, idRaza, stock):
        self.idRaza = idRaza
        self.stock = stock

    @property
    def idRaza(self):
        return self.idRaza

    @idRaza.setter
    def idRaza(self, value):
        if not value:
            raise TypeError("Es obligatorio indicar la raza")
        self.idRaza = value

    @property
    def stock(self):
        return self.stock

    @stock.setter
    def stock(self, value):
        if value <= 0:
            raise ValueError("Debe ingresar una cantidad mayor a 0")
        self.stock = value
