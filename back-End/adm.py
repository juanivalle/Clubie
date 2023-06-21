from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import random
import string
from flask_bcrypt import Bcrypt
from clases import *
from flask_login import UserMixin

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.username

    @staticmethod
    def get_by_username(username):
        users = [
            User('jugador', 'numeroso'),
        ]
        for user in users:
            if user.username == username:
                return user
        return None
    def check_password(self, password):
        return self.password == password
    
"""Modificar los campos para que queden acorde a la base de datos y no con self"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return
    return render_template('login.html', form=form)

@app.route('/admin', methods=['GET'])
@login_required
def admin():
    # Resto del código para la página de administración
    return render_template('PAGINAADMIN.html')
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

def generate_user_credentials():
    username = generate_random_string(6)
    password = generate_random_string(12)
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return username, password, hashed_password

"""CONECTAR ESTE USUARIO CON EL LOGINPAGE DE LA OTRA PAGINA"""

"""LA PAGINA DE ARRIBA DEBERIA SER PARA ENTRAR A LA PAGINA PARA LOG DE ADMIN"""

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
