from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)
