from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, text
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import FileField, FileAllowed, FileSize
from flask_bcrypt import check_password_hash, Bcrypt
from rutas import *
from clases import *



login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(cedula):
    return User.query.get(int(cedula))

@app.route('/')
@app.route('/home.html')
def index():
    usuarios = User.query.all()
    return render_template("/noLog/home.html", usuarios=usuarios)

@app.route('/registerform', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        form = RegistrationForm()

        if form.validate_on_submit():
            cedula = form.cedula.data
            name = form.name.data
            telefono =form.telefono.data
            email = form.email.data        
            user = User.query.filter(or_(
                User.cedula == cedula, User.name == name, User.telefono == telefono, User.email == email)).first()
            if user:
                return redirect(url_for('home'))        
            new_user = User(cedula=cedula, name=name,
                            telefono=telefono, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('miembros'))
        return redirect(url_for('login'))
    
@app.route('/miembros.html')
def miembros():
    usuarios = User.query.all()
    return render_template('/logueado/miembros.html', users=usuarios)

# FUNCION QUE SE ENCARGARA DE ELIMINAR SOCIOS DEL CLUB // FUNCIONA
@app.route('/delete/<cedula>')
def delete_socio(cedula):
    query = text('DELETE FROM user WHERE cedula = :cedula')
    db.session.execute(query, {'cedula': cedula})
    db.session.commit()
    return redirect(url_for('miembros'))



def update_user(cedula):
    form = EditForm()
    usuario = User.query.get_or_404(cedula)

    if form.validate_on_submit():
        usuario.cedula = form.cedula.data
        usuario.name = form.name.data
        usuario.telefono =form.telefono.data
        usuario.email = form.email.data
        db.session.commit()
        return redirect(url_for('miembros'))

    form = EditForm(obj=usuario)
    return render_template('/logueado/edit_usuario.html', form=form, usuario=usuario)

    

@app.route('/edit/<cedula>', methods=['GET'])
#@login_required
def editar_usuario(cedula):
    form = EditForm(obj=User)
    usuario = User.query.get_or_404(cedula)

    return render_template('/logueado/edit_usuario.html', form=form, usuario=usuario)


# @app.route('/eliminar/<string:user_cedula>', methods=['POST'])
# def eliminar_usuario(user_cedula):
#     usuario = User.query.filter_by(cedula=user_cedula).first_or_404()
#     db.session.delete(usuario)
#     db.session.commit()
#     return redirect(url_for('miembros'))







@app.route('/contact.html')
def contact():
    return render_template('/noLog/contact.html')

@app.route('/login.html')
def login():
    return render_template('/noLog/login.html')

@app.route('/nosotros.html')
def nosotros():
    return render_template('/noLog/nosotros.html')

@app.route('/equipo.html')
def equipo():
    return render_template('/noLog/equipo.html')

@app.route('/road-map.html')
def roadMap():
    return render_template('/noLog/road-map.html')

@app.route('/home-club.html')
def home_club():
    return render_template('/logueado/home-club.html')



@app.route('/ventas.html')
def ventas():
    return render_template('/logueado/ventas.html')

@app.route('/trasabilidad.html')
def trasabilidad():
    return render_template('/logueado/trasabilidad.html')

@app.route('/ctrplanta.html')
def ctrplanta():
    return render_template('/logueado/ctrplanta.html')


@app.route('/graficos.html')
def graficos():
    return render_template('/logueado/graficos.html')






























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