#!/usr/bin/python3
"""Creation of the diferent clases that we need"""
#CAMBIAR REGISTER DE USUARIO POR LA PAGINA DOPNDE SUBE DATA EL CLUB Y PONER REGISTER PARA EL CLUB
from uuid import uuid4
import re #
from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import FileField, FileAllowed, FileSize
import random
import hashlib
from flask_bcrypt import check_password_hash, Bcrypt
from app import create_app, db
from sqlalchemy import or_


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(8), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(30), nullable=False)

class RegistrationForm(Form):
    username = StringField('username', [validators.Length(min=6, max=25)])
    cedula = IntegerField('cedula', [validators.Length(min=7, max=8)])
    email = StringField('email', [validators.Length(min=6, max=35)])
    password = PasswordField('password', [
        validators.DataRequired()
    ])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
#CAMBIAR EL CEDULA.EMAIL.DATA
    if form.validate_on_submit():
        cedula = cedula.email.data
        username = form.username.data
        password = form.password.data
        email = form.email.data

        user = User.query.filter(or_(User.cedula == cedula, User.username == username, User.email == email)).first()
        if user:
            response = jsonify({'message': 'El usuario ya existe'})
            response.headers['Fail-SweetAlert'] = 'error'
            return redirect(url_for('register'))

        new_user = User(cedula=cedula, username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()

        response = jsonify({'message': 'Registrado exitosamente'})
        response.headers['Fail-SweetAlert'] = 'success'
        return redirect(url_for('login'))

    return render_template('register.html', form=form)



class Club():
    id = db.Column(db.Integer, primary_key=True)
    campoarchivo = db.Column(db.String(30, nullable=False))
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(70))




#Es importante tener en cuenta que, para que el formulario se muestre correctamente en la vista, es necesario 
# renderizarlo usando una plantilla de Jinja2 y agregar el atributo enctype="multipart/form-data" al formulario para permitir la carga de archivos.
class ClubForm(Form):
    campoarchivo = FileField('campoarchivo', validators=[
        DataRequired(message='Por favor seleccione un archivo.'),
        FileAllowed(['jpg', 'jpeg', 'png']),
        FileSize(max_size=10 * 1024 * 1024)
#ESTA ES LA PARTE DEL ARCHIVO
])
    #FALTA DIRECCION, DUEÑO, CAPAZ ALGO MAS
    username = StringField('username', [validators.Length(min=6, max=25)])
    email = StringField('email', [validators.Length(min=6, max=35)])
    password = PasswordField('password', [
        validators.DataRequired()
    ])

@app.route('/register', methods=['GET', 'POST'])
def clubes():
    form = ClubForm()

    if form.validate_on_submit():


  # procesa el formulario y guarda los datos en la base de datos


        # Si todo va bien, redirige a otra página que seria la del registro del club como puede ser el login
        return redirect(url_for('otra_pagina'))

    # Si hay algún error en la validación del formulario, muestra una SweetAlert como la de arriba
    errors = form.errors.items()
    if errors:
        response = jsonify({'message': 'El usuario ya existe'})
        response.headers['Fail-SweetAlert'] = 'error'
        return render_template('clubes.html', form=form)

    return render_template('clubes.html', form=form)


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Usuario"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Contraseña"})
    
    submit = SubmitField("Iniciar")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('login.html')
    else:
        return render_template('login.html')

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
