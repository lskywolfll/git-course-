import pickle
lista_nombres=["Pedro", "ana", "Maria", "Isabel"]
#metodo open, nombre de la carpeta, con que permiso crear el archivo y binaria es wb
fichero_binario=open("lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario)