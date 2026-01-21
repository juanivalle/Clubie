from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SelectField, SubmitField, validators
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, Email, Length, InputRequired, Optional, NumberRange, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileSize
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from rutas import *
from datetime import datetime
import os


# Configuración segura de SECRET_KEY
# En producción, DEBE configurarse la variable de entorno SECRET_KEY
import secrets
_secret_key = os.environ.get('SECRET_KEY')
if not _secret_key:
    # En desarrollo: genera una clave aleatoria (cambia en cada reinicio)
    # En producción: DEBE configurarse la variable de entorno
    _secret_key = secrets.token_hex(32)
    print("⚠️  ADVERTENCIA: SECRET_KEY no configurada. Usando clave temporal.")
    print("   En producción, configure la variable de entorno SECRET_KEY")
app.config['SECRET_KEY'] = _secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    cedula = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.now)
    
    # Relación con Club
    club = db.relationship('Club', backref='miembros_club', lazy=True)
    
    # Relación con ventas
    ventas = db.relationship('Ventas', backref='usuario', lazy=True)
    
    def __repr__(self):
        return f'<User {self.name}>'

class RegistrationForm(FlaskForm):
    name = StringField('Nombre Completo', validators=[DataRequired(), Length(min=3, max=50, message='El nombre debe tener entre 3 y 50 caracteres')])
    cedula = IntegerField('Cédula', validators=[DataRequired(), NumberRange(min=1000000, max=99999999, message='Cédula inválida')])
    telefono = IntegerField('Teléfono', validators=[DataRequired(), NumberRange(min=10000000, max=999999999, message='Teléfono inválido')])
    email = StringField('Email', validators=[DataRequired(), Email(message='Email inválido'), Length(max=50)])
    submit = SubmitField('Registrar Miembro')

class EditForm(FlaskForm):
    cedula = StringField('cedula', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar cambios')

class Club(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    campoarchivo = db.Column(db.String(30))
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(70))
    is_superuser = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)
    
    def set_password(self, password):
        """Hashea y guarda la contraseña"""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        """Verifica la contraseña contra el hash"""
        return bcrypt.check_password_hash(self.password_hash, password)

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(message='Usuario requerido'), Length(min=4, max=20, message='Usuario debe tener entre 4 y 20 caracteres')], render_kw={"placeholder": "Usuario"})
    password = PasswordField('Contraseña', validators=[InputRequired(message='Contraseña requerida'), Length(min=4, max=30, message='Contraseña debe tener entre 4 y 30 caracteres')], render_kw={"placeholder": "Contraseña"})
    submit = SubmitField("Iniciar Sesión")

class Trazabilidad(db.Model):
    idplanta = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    raza = db.Column(db.String(30), nullable=False)
    Enraizado = db.Column(db.DateTime, nullable=True)
    Riego = db.Column(db.DateTime, nullable=True)
    paso1 = db.Column(db.DateTime, nullable=True)
    paso2 = db.Column(db.DateTime, nullable=True)
    paso3 = db.Column(db.DateTime, nullable=True)
    floracion = db.Column(db.DateTime, nullable=True)
    cosecha = db.Column(db.DateTime, nullable=True)
    cantidad = db.Column(db.String(3), nullable=False)
    observaciones = db.Column(db.String(80), nullable=True)

class PlantForm(FlaskForm):
    idplanta = IntegerField('idplanta')
    raza = StringField('raza')    
    Enraizado = DateTimeLocalField('Enraizado', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    Riego = DateTimeLocalField('Riego', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso1 = DateTimeLocalField('paso1', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso2 = DateTimeLocalField('paso2', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso3 = DateTimeLocalField('paso3', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    floracion = DateTimeLocalField('floracion', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    cosecha = DateTimeLocalField('cosecha', format='%Y-%m-%dT%H:%M', validators=[Optional()])

    cantidad = StringField('cantidad')
    observaciones = StringField('observaciones')

class Ventasform(FlaskForm):
    cedulaVenta = SelectField('cedulaVenta')
    razaVenta = StringField('razaVenta')
    cantVenta = IntegerField('cantVenta')
    retiro = DateTimeLocalField('retiro', format='%Y-%m-%dT%H:%M')

class Ventas(db.Model):
    idventas = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    cedula = db.Column(db.Integer, db.ForeignKey('user.cedula'), nullable=False)
    raza = db.Column(db.String(30), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    retiro = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f'<Venta {self.idventas}: {self.cantidad}g de {self.raza}>'


# ================================================================================
# MODELO Y FORMULARIOS PARA MIEMBROS (USUARIOS FINALES)
# ================================================================================

class Member(db.Model, UserMixin):
    """Cuenta de login para miembros de clubs (usuarios finales)"""
    id = db.Column(db.Integer, primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    cedula = db.Column(db.Integer, db.ForeignKey('user.cedula'), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.now)
    
    # Relación con User (datos del miembro en el club)
    usuario = db.relationship('User', backref='cuenta_member', lazy=True)
    
    def set_password(self, password):
        """Hashea y guarda la contraseña"""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        """Verifica la contraseña contra el hash"""
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def get_id(self):
        """Retorna ID con prefijo para diferenciar de Club"""
        return f"member_{self.id}"
    
    def __repr__(self):
        return f'<Member {self.email}>'


class MemberRegistrationForm(FlaskForm):
    """Formulario de registro para miembros"""
    cedula = IntegerField('Cédula', validators=[
        DataRequired(message='La cédula es requerida'),
        NumberRange(min=1000000, max=99999999, message='Cédula inválida')
    ], render_kw={"placeholder": "Tu número de cédula"})
    
    email = StringField('Email', validators=[
        DataRequired(message='El email es requerido'),
        Email(message='Email inválido'),
        Length(max=70)
    ], render_kw={"placeholder": "tu@email.com"})
    
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es requerida'),
        Length(min=8, max=30, message='La contraseña debe tener entre 8 y 30 caracteres')
    ], render_kw={"placeholder": "Mín. 8 caracteres, 1 mayúscula, 1 número, 1 símbolo"})
    
    def validate_password(self, password):
        """Valida complejidad de la contraseña"""
        p = password.data
        if not any(c.isupper() for c in p):
            raise ValidationError('La contraseña debe incluir al menos una mayúscula.')
        if not any(c.isdigit() for c in p):
            raise ValidationError('La contraseña debe incluir al menos un número.')
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in p):
            raise ValidationError('La contraseña debe incluir al menos un carácter especial (!@#$%).')
    
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        DataRequired(message='Confirma tu contraseña')
    ], render_kw={"placeholder": "Repite tu contraseña"})
    
    submit = SubmitField("Crear Cuenta")


class MemberLoginForm(FlaskForm):
    """Formulario de login para miembros"""
    email = StringField('Email', validators=[
        DataRequired(message='El email es requerido'),
        Email(message='Email inválido')
    ], render_kw={"placeholder": "tu@email.com"})
    
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es requerida')
    ], render_kw={"placeholder": "Tu contraseña"})
    
    submit = SubmitField("Iniciar Sesión")


class ContactForm(FlaskForm):
    """Formulario de contacto al club"""
    asunto = StringField('Asunto', validators=[
        DataRequired(message='El asunto es requerido'),
        Length(max=100)
    ], render_kw={"placeholder": "¿En qué podemos ayudarte?"})
    
    mensaje = StringField('Mensaje', validators=[
        DataRequired(message='El mensaje es requerido'),
        Length(max=500)
    ], render_kw={"placeholder": "Escribe tu mensaje aquí..."})
    
    submit = SubmitField("Enviar Mensaje")


# ================================================================================
# MODELO Y FORMULARIO PARA PEDIDOS (COORDINACIÓN DE COMPRAS)
# ================================================================================

class Pedido(db.Model):
    """Solicitud de coordinación de compra de un miembro"""
    id = db.Column(db.Integer, primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    cedula = db.Column(db.Integer, db.ForeignKey('user.cedula'), nullable=False)
    raza = db.Column(db.String(30), nullable=False)
    cantidad_solicitada = db.Column(db.Integer, nullable=False)
    mensaje = db.Column(db.String(200), nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.now)
    estado = db.Column(db.String(20), default='pendiente')  # pendiente, coordinado, completado, cancelado
    
    # Relación con User
    usuario = db.relationship('User', backref='pedidos', lazy=True)
    
    def __repr__(self):
        return f'<Pedido {self.id}: {self.cantidad_solicitada}g de {self.raza}>'


class PedidoForm(FlaskForm):
    """Formulario para solicitar coordinación de pedido"""
    raza = SelectField('Raza', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad (gramos)', validators=[
        DataRequired(message='Indica la cantidad'),
        NumberRange(min=1, max=100, message='Cantidad entre 1 y 100 gramos')
    ], render_kw={"placeholder": "Ej: 10"})
    mensaje = StringField('Mensaje (opcional)', validators=[
        Length(max=200)
    ], render_kw={"placeholder": "¿Cuándo podrías pasar a retirarlo?"})
    submit = SubmitField("Coordinar Pedido")