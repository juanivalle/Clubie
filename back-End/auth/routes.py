from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from forms import LoginForm, RegistrationForm
from models import User
from extensions import db, login_manager


bp = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route('/login', methods=['GET', 'POST'])
@bp.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next_url = request.args.get('next') or url_for('main.home')
            return redirect(next_url)
        flash('Credenciales inválidas', 'error')
    return render_template('noLog/login.html', form=form)


@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter((User.email == form.email.data.lower()) | (User.cedula == form.cedula.data)).first():
            flash('Usuario ya existe', 'error')
            return redirect(url_for('auth.register'))
        user = User(
            cedula=form.cedula.data,
            name=form.name.data,
            telefono=form.telefono.data,
            email=form.email.data.lower(),
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registro exitoso, ahora puedes iniciar sesión', 'success')
        return redirect(url_for('auth.login'))
    return render_template('noLog/login.html', form=form)

