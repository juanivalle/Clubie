from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import FileField, FileAllowed, FileSize

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(8), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(30), nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('username', [validators.Length(min=6, max=25)])
    cedula = IntegerField('cedula', [validators.Length(min=7, max=8)])
    email = StringField('email', [validators.Length(min=6, max=35)])
    password = PasswordField('password', [
        validators.DataRequired()
    ])

class Club():
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

class Plant(FlaskForm):
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