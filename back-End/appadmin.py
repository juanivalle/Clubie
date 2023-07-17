from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3
from clases import *

app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def Index():
    cursor = db().cursor()
    cursor.execute('SELECT * FROM clubes')
    data = cursor.fetchall()
    return render_template('registro.html', clubes = data)


"""@app.route('/add_club', methods=['POST'])
def add_contact():
    # Funcion que añade un nuevo club a la base de datos
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        direccion = request.form['direccion']
        cursor = db().cursor()
        cursor.execute('INSERT INTO clubes (nombre, email, phone, direccion) VALUES (?, ?, ?, ?)',
                       (fullname, email, phone, direccion))
        db().commit()
        return redirect(url_for('Index'))"""

# @app.route('/delete/<string:id>')
# def delete_club(id):
#     cursor = db().cursor()
#     cursor.execute('DELETE FROM clubes WHERE id = ?',(id,))
#     db().commit()
#     return redirect(url_for('Index'))

# @app.route('/edit/<id>')
# def get_contact(id):
#     cursor = db().cursor()
#     cursor.execute('SELECT * FROM clubes WHERE id = ?',(id,))
#     data = cursor.fetchall()
#     return render_template('edit-club.html', club = data[0])

# @app.route('/update/<id>', methods=['POST'])
# def update_club(id):
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         email = request.form['email']
#         phone = request.form['phone']
#         direccion = request.form['direccion']

#         cursor = db().cursor()
#         cursor.execute("""
#             UPDATE clubes
#             SET nombre = ?,
#                 email = ?,
#                 phone = ?,
#                 direccion = ?
#             WHERE id = ?
#         """, (fullname, email, phone, direccion, id))
#         db().commit()
#         return redirect(url_for('Index'))

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
        

#     app.run(port=5000, debug=True)
