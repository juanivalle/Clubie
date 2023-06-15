from flask import Flask, render_template

app = Flask(__name__, static_folder='../css')






if __name__ == '__main__':
    app.run(debug=True)