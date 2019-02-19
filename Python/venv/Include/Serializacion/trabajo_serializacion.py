import pickle
#comvertir a binario read binary
fichero = open("lista_nombres", "rb")

lista = pickle.load(fichero)

print(lista)