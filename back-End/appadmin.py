from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    # Función para obtener la conexión a la base de datos SQLite
    db = getattr(g, 'sqlite_db', None)
    if db is None:
        db = g.sqlite_db = sqlite3.connect('adminClubie.db')
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_db(error):
    # Función para cerrar la conexión a la base de datos SQLite al final de la solicitud
    db = getattr(g, 'sqlite_db', None)
    if db is not None:
        db.close()

@app.route('/')
def Index():
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM clubes')
    data = cursor.fetchall()
    return render_template('registro.html', clubes = data)

@app.route('/add_club', methods=['POST'])
def add_contact():
    # Funcion que añade un nuevo club a la base de datos
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        direccion = request.form['direccion']
        cursor = get_db().cursor()
        cursor.execute('INSERT INTO clubes (nombre, email, phone, direccion) VALUES (?, ?, ?, ?)',
                       (fullname, email, phone, direccion))
        get_db().commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_club(id):
    cursor = get_db().cursor()
    cursor.execute('DELETE FROM clubes WHERE id = ?',(id,))
    get_db().commit()
    return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_contact(id):
    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM clubes WHERE id = ?',(id,))
    data = cursor.fetchall()
    return render_template('edit-club.html', club = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_club(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        direccion = request.form['direccion']

        cursor = get_db().cursor()
        cursor.execute("""
            UPDATE clubes
            SET nombre = ?,
                email = ?,
                phone = ?,
                direccion = ?
            WHERE id = ?
        """, (fullname, email, phone, direccion, id))
        get_db().commit()
        return redirect(url_for('Index'))

if __name__ == '__main__':
    with app.app_context():
        cursor = get_db().cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS clubes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre VARCHAR(255),
                            email VARCHAR(255),
                            phone VARCHAR(20),
                            direccion VARCHAR(255))''')
        get_db().commit()

    app.run(port=5000, debug=True)
