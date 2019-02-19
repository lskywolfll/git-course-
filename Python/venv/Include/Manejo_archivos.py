from io import open
#Abreviaciones de la plabra r púede cambiar para w escribir en ingles
archivo_texto = open("archivo.txt", "r+")

#r- read w-write a-append / r+ = leer y escribir
"""frase = "Estupendo dia para estudiar python \n el miercoles"

archivo_texto.write(frase)

texto = archivo_texto.read()

archivo_texto.close()

print(texto)

lineas_texto = archivo_texto.readlines()

archivo_texto.close()

archivo_texto.write("\n siempre es una buena ocasion para estudiar python")

archivo_texto.close()

print(archivo_texto.read())
#posicion en el caracter 0 - el que quieras
archivo_texto.seek(0)

print(archivo_texto.read())

archivo_texto.write("comienzo del texto")

#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()

lista_texto[1]=" esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()"""
