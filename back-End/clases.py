#!/usr/bin/python3
"""Creation of the diferent clases that we need"""
import uuid4
import re #

class User():
    """Define the new class User"""
    def __init__(self, name, pwd, email, pType):
        self.id = str(uuid4)
        self.name = name
        self.__pwd = pwd
        self.email = email
        self.type = pType

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError("El nombre no puede contener números")
        if not value:
            raise ValueError("Es obligatorio el ingreso de su Nombre")
        self.name = value

    @property
    def pwd(self):
        return self.__pwd

    @pwd.setter
    def pwd(self, value):
        if len(value) < 8:
            raise TypeError("La contraseña debe tener como mínimo 8 caracteres")
        if isdigit(str(value)) == False:
            raise TypeError("La contraseña debe tener al menos un número")
        self.__pwd = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if re.match(expresion_regular, value) is not None:
            self.email = value
        else:
            raise TypeError("Ingrese un email válido")

class Plant():
    """Define the new class Plant"""
    def __init__(self, idRaza, cantidad, riego, sustrato, cortes, Luz, Poda, residuos):
        self.idRaza = idRaza
        self.cantidad = cantidad
        self.riego = riego
        self.sustrato = sustrato
        self.cortes = cortes
        self.luz = Luz
        self.poda = Poda
        self.residuos = residuos

    @property
    def idRaza(self):
        return self.idRaza

    @idRaza.setter
    def idRaza(self, value):
        if not value:
            raise TypeError("Es obligatorio indicar la raza")
        self.idRaza = value

    # SIN TERMINAR

class Cogo():
    """Define the new class Cogo"""
    def __init__(self, idRaza, stock):
        self.idRaza = idRaza
        self.stock = stock

    @property
    def idRaza(self):
        return self.idRaza

    @idRaza.setter
    def idRaza(self, value):
        if not value:
            raise TypeError("Es obligatorio indicar la raza")
        self.idRaza = value

    @property
    def stock(self):
        return self.stock

    @stock.setter
    def stock(self, value):
        if value <= 0:
            raise ValueError("Debe ingresar una cantidad mayor a 0")
        self.stock = value
