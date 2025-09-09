import os
from flask import Flask
from dotenv import load_dotenv
from extensions import init_extensions, db


class DefaultConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(os.path.dirname(__file__), 'instance', 'app.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'


def ensure_instance_dir(app: Flask) -> None:
    instance_dir = os.path.join(os.path.dirname(__file__), 'instance')
    os.makedirs(instance_dir, exist_ok=True)


def create_app(config_object: str | None = None) -> Flask:
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(DefaultConfig)
    if config_object:
        app.config.from_object(config_object)

    ensure_instance_dir(app)
    init_extensions(app)

    # Blueprints will be registered later after creation
    from auth.routes import bp as auth_bp  # type: ignore
    from main.routes import bp as main_bp  # type: ignore
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    @app.before_first_request
    def _create_tables_if_needed():
        db.create_all()

    return app

