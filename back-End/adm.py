from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import random
import hashlib
from flask_bcrypt import check_password_hash, Bcrypt
from app import create_app, db


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(6), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

"""GENERA usuario y password aleatorio de 6 caracteres si no me equivoco"""
def generate_username(length):
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    username = ''.join(random.choice(characters) for i in range(length))
    return username


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def hash_password(password):
    """ESTO NO SE QUE TAN NECESARIO ES PERO ES UN CIFRADO DE CONTRASEÑAS"""
    salt = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest().encode('utf-8')
    hash = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    return (salt + hash).decode('utf-8')

"""No se como puedo ac"""
@app.route('/new_user', methods=['POST'])
def new_user():
    if current_user.is_authenticated and current_user.is_superuser():
        new_user = User(username=generate_username(6), password=hash_password(generate_password(6)))
        db.session.add(new_user)
        db.session.commit()


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Usuario"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Contraseña"})
    
    submit = SubmitField("Iniciar")

"""SUPER USUARIO"""
app = create_app()
with app.app_context():
    db.create_all()

    superuser = User(username='Moria3', is_superuser=True)
    superuser.set_password('Kiko01')
    db.session.add(superuser)
    db.session.commit()


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('votacion.html'))
        else:
            ValidationError("Usuario o contraseña equivocado")
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)