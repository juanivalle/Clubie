from flask import Flask, render_template
from flask_cors import CORS
import os


app = Flask(__name__)

# CORS configuración segura - limitar orígenes en producción
# En desarrollo permite localhost, en producción usar variable de entorno
allowed_origins = os.environ.get('CORS_ORIGINS', 'http://localhost:5000,http://127.0.0.1:5000').split(',')
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

if __name__ == '__main__':
    # Debug mode controlado por variable de entorno (deshabilitado por defecto)
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host="localhost", port="5000", debug=debug_mode)

