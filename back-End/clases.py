from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import FileField, FileAllowed, FileSize
from rutas import *
from datetime import datetime

app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    cedula = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)

class RegistrationForm(FlaskForm):

    cedula = IntegerField('cedula', validators=[validators.NumberRange(min=1000000, max=99999999)])
    name = StringField('name', validators=[validators.Length(min=6, max=25)])
    telefono = IntegerField('telefono', validators=[validators.NumberRange(min=100000000, max=999999999)])
    email = StringField('email', validators=[validators.Length(min=6, max=35)])

    # password = PasswordField('password', [
    #     validators.DataRequired()
    # ])

class EditForm(FlaskForm):
    cedula = StringField('Cédula', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar cambios')


class ClubForm(FlaskForm):
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
class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campoarchivo = db.Column(db.String(30))
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(70))
















class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Usuario"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Contraseña"})
    
    submit = SubmitField("Iniciar")

class Trazabilidad(db.Model):
    """Define the new class Plant"""
    idraza = db.Column(db.Integer, primary_key=True, autoincrement=True)
    raza = db.Column(db.String(30), nullable=False)
    enraizado = db.Column(db.String(30), nullable=False)
    paso1 = db.Column(db.DateTime, nullable=True)
    paso2 = db.Column(db.DateTime, nullable=True)
    paso3 = db.Column(db.DateTime, nullable=True)
    floracion = db.Column(db.String(30), nullable=False)
    cosecha = db.Column(db.String(30), nullable=False)
    cantidad = db.Column(db.String(30))
    observaciones = db.Column(db.String(30), nullable=False)
    #PREGUNTAR ESTO: riego = db.Column(db.String(30), unique=True, nullable=False)
    #PREGUNTAR ESTO: sustrato = db.Column(db.String(25), nullable=False)
    #PREGUNTAR ESTO: cortes = db.Column(db.String(70))
    #PREGUNTAR ESTO: luz= db.Column(db.String(70))
    #PREGUNTAR ESTO: poda= db.Column(db.String(70))
    #PREGUNTAR ESTO: residuos= db.Column(db.String(70))

class PlantForm(FlaskForm):
    idraza = IntegerField('idRaza')
    raza = StringField('Raza')
    enraizado = StringField('Enraizado')
    paso1 = DateTimeLocalField('Paso 1')
    paso2 = DateTimeLocalField('Paso 2')
    paso3 = DateTimeLocalField('Paso 3')
    floracion = StringField('Floración')
    cosecha = StringField('Cosecha' )
    cantidad = StringField('Cantidad')
    observaciones = StringField('Observaciones')
  ##FIJARSE SI LOS CAMPOS ESTAN BIEN, SI ESTAN BIEN PONER VALIDADORES COMO EN "REGISTRATION FORM"


##NO SE SI CANTIDAD ES LOS COGOLLOS, O COSECHA, ESO FALTA PARA PODER CONECTAR
class Ventasform(FlaskForm):
    idventas = IntegerField('idRaza')
    cantidad = StringField('cantidad')
    retiro = StringField('retiro')




class Ventas(db.Model):
    idventas = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    cantidad = db.Column(db.String(30), nullable=False)
    retiro = db.Column(db.String(12), default=datetime.now())