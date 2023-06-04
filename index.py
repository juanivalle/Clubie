from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    port = 3307,
    password = "",
    database = "clubie"
)

myCursor = mydb.cursor()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/signup', methods=['POST'])
def singup():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        tel = request.form.get("tel")
        password = request.form.get("pass")
        mail = request.form.get("mail")
        dir = request.form.get("dir")
        query = f"INSERT INTO users (Name, Phone, Password, Mail, Address) VALUES ('{fullname}', '{tel}', '{password}', '{mail}', '{dir}')"
        myCursor.execute(query)
        mydb.commit()
        return (redirect(url_for('index')))
    else:
        return "bad request"
    #return render_template('register.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
