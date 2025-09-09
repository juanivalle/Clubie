from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db


class User(UserMixin, db.Model):
    cedula = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    ventas = db.relationship('Ventas', backref='usuario', lazy=True)

    def get_id(self) -> str:
        return str(self.cedula)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Trazabilidad(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    raza = db.Column(db.String(30), nullable=False)
    Enraizado = db.Column(db.DateTime, nullable=True)
    Riego = db.Column(db.DateTime, nullable=True)
    paso1 = db.Column(db.DateTime, nullable=True)
    paso2 = db.Column(db.DateTime, nullable=True)
    paso3 = db.Column(db.DateTime, nullable=True)
    floracion = db.Column(db.DateTime, nullable=True)
    cosecha = db.Column(db.DateTime, nullable=True)
    cantidad = db.Column(db.Integer, nullable=False)
    observaciones = db.Column(db.String(120), nullable=True)


class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_cedula = db.Column(db.Integer, db.ForeignKey('user.cedula'), nullable=False, index=True)
    raza = db.Column(db.String(30), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    retiro = db.Column(db.DateTime, default=datetime.utcnow)

