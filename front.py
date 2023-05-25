from flask import Flask, render_template

app = Flask(__name__, static_folder='css')

@app.route('/')
@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/nosotros.html')
def nosotros():
    return render_template('nosotros.html')

@app.route('/home-club.html')
def home_club():
    return render_template('home-club.html')

@app.route('/miembros.html')
def miembros():
    return render_template('miembros.html')

@app.route('/ventas.html')
def ventas():
    return render_template('ventas.html')

@app.route('/trasabilidad.html')
def trasabilidad():
    return render_template('trasabilidad.html')

@app.route('/ctrplanta.html')
def ctrplanta():
    return render_template('ctrplanta.html')


if __name__ == '__main__':
    app.run(debug=True)