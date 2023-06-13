from flask import Flask, render_template, url_for, redirect, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import FileField, FileAllowed, FileSize
from flask_bcrypt import check_password_hash, Bcrypt

from rutas import *
from clases import *




@app.route('/registerform', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        cedula = form.cedula.data
        name = form.name.data
        telefono = form.telefono.data
        email = form.email.data

        user = User.query.filter(or_(
            User.cedula == cedula, User.name == name, User.telefono == telefono, User.email == email)).first()
        if user:
            return redirect(url_for('roadMap'))

        new_user = User(cedula=cedula, name=name,
                        telefono=telefono, email=email)
        db.session.add(new_user)
        db.session.commit()
        all_users = User.query.all()
        for user in all_users:
            print(user.cedula, user.name, user.telefono, user.email)

       
        return redirect(url_for('login'))

    return redirect(url_for('miembros', form=form))


# Es importante tener en cuenta que, para que el formulario se muestre correctamente en la vista, es necesario
# renderizarlo usando una plantilla de Jinja2 y agregar el atributo enctype="multipart/form-data" al formulario para permitir la carga de archivos.


# @app.route('/register', methods=['GET', 'POST'])
# def clubes():
#     form = ClubForm()

#     if form.validate_on_submit():

#       # procesa el formulario y guarda los datos en la base de datos

#         # Si todo va bien, redirige a otra página que seria la del registro del club como puede ser el login
#         return redirect(url_for('otra_pagina'))

#     # Si hay algún error en la validación del formulario, muestra una SweetAlert como la de arriba
#     errors = form.errors.items()
#     if errors:
#         response = jsonify({'message': 'El usuario ya existe'})
#         response.headers['Fail-SweetAlert'] = 'error'
#         return render_template('clubes.html', form=form)



# @app.route('/loginform', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         nombre = request.form['nombre']  # Obtiene el valor del campo "nombre"
#     edad = request.form['edad'] 

#     if request.method == 'POST':
#         print(request.form['username'])
#         print(request.form['password'])
#         return render_template('login.html')
#     else:
#         return render_template('login.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        

    app.run(port=5000, debug=True)