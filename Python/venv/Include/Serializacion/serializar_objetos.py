import pickle

class Vehiculos():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frena(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


coche1 = Vehiculos("Mazda","MX5")
coche2 = Vehiculos("Renault","MX5")
coche3 = Vehiculos("mitsubishi","MX5")

coches = [coche1, coche2, coche3]
#1-Nombre a dar al archio 2- tipo de acciones para leer escribir binario entre otros
fichero = open("losCoches", "wb")
#volcado de informacion
pickle.dump(coches,fichero)

fichero.close()

del (fichero)

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())