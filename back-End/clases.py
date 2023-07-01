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
    telefono = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[validators.Length(min=6, max=25)])
    cedula = IntegerField('cedula', validators=[validators.NumberRange(min=1000000, max=99999999)])
    telefono = IntegerField('telefono', validators=[validators.NumberRange(min=10000000, max=999999999)])
    email = StringField('email', validators=[validators.Length(min=6, max=35)])



class EditForm(FlaskForm):
    cedula = StringField('cedula', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar cambios')


class ClubForm(FlaskForm):
    campoarchivo = FileField('campoarchivo', validators=[
        DataRequired(message='Por favor seleccione un archivo.'),
        FileAllowed(['jpg', 'jpeg', 'png']),
        FileSize(max_size=10 * 1024 * 1024)
#ESTA ES LA PARTE DEL ARCHIVO
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
    raza = StringField('raza')
    enraizado = StringField('Enraizado')
    paso1 = DateTimeLocalField('paso1')
    paso2 = DateTimeLocalField('paso2')
    paso3 = DateTimeLocalField('paso3')
    floracion = StringField('floracion')
    cosecha = StringField('cosecha' )
    cantidad = StringField('cantidad')
    observaciones = StringField('observaciones')
  ##FIJARSE SI LOS CAMPOS ESTAN BIEN, SI ESTAN BIEN PONER VALIDADORES COMO EN "REGISTRATION FORM"


##NO SE SI CANTIDAD ES LOS COGOLLOS, O COSECHA, ESO FALTA PARA PODER CONECTAR
class Ventasform(FlaskForm):
    idventas = IntegerField('idRaza')
    cedula = IntegerField('cedula')
    raza = StringField('raza')
    cantidad = StringField('cantidad')
    retiro = DateTimeLocalField('retiro')




class Ventas(db.Model):
    idventas = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    cedula = StringField('cedula')
    idraza = IntegerField('idRaza')
    cantidad = db.Column(db.String(30), nullable=False)
    retiro = db.Column(db.String(12), default=datetime.now())
    total_ventas = db.Column(db.Integer, default=0)