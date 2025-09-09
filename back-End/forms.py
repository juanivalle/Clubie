from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateTimeLocalField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField('Ingresar')


class RegistrationForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=30)])
    cedula = IntegerField('Cédula', validators=[DataRequired(), NumberRange(min=1)])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField('Registrar')


class EditForm(FlaskForm):
    cedula = IntegerField('Cédula', validators=[DataRequired(), NumberRange(min=1)])
    name = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=30)])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    submit = SubmitField('Guardar cambios')


class PlantForm(FlaskForm):
    raza = StringField('Raza', validators=[DataRequired(), Length(min=1, max=30)])
    Enraizado = DateTimeLocalField('Enraizado', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    Riego = DateTimeLocalField('Riego', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso1 = DateTimeLocalField('Paso 1', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso2 = DateTimeLocalField('Paso 2', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso3 = DateTimeLocalField('Paso 3', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    floracion = DateTimeLocalField('Floración', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    cosecha = DateTimeLocalField('Cosecha', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=0)])
    observaciones = StringField('Observaciones')
    submit = SubmitField('Guardar')


class VentasForm(FlaskForm):
    cedulaVenta = SelectField('Cédula', coerce=int)
    razaVenta = StringField('Raza', validators=[DataRequired(), Length(min=1, max=30)])
    cantVenta = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)])
    retiro = DateTimeLocalField('Retiro', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    submit = SubmitField('Vender')

