from flask import Flask, render_template

class Programa:
    def __init__(self):
        self.app=Flask(__name__)

        #Crear url
        self.app.add_url_rule('/nuevo', view_func=self.agregar)

        #Iniciar el Server
        self.app.run(debug=True)

    def agregar(self):
        return render_template('nuevoClub.html')
    
miPrograma = Programa()