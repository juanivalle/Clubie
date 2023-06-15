from flask import Flask, render_template

app = Flask(__name__, static_folder='../css')



@app.route('/contact.html')
def contact():
    return render_template('/noLog/contact.html')

@app.route('/login.html')
def login():
    return render_template('/noLog/login.html')

@app.route('/nosotros.html')
def nosotros():
    return render_template('/noLog/nosotros.html')

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


if __name__ == '__main__':
    app.run(debug=True)