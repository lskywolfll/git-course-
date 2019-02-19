"""miLista= ["maria", "pepe", "Marta", "Antonio"]

miLista.extend(["sandra","ana","Lucia"])

print(miLista.index("ana"))"""

#Tupla es muy similar a los array pero no se puede manipular del todo y es mas rapida

"""miLista = ["juan", 13, 1, 1995]
miTupla = tuple(miLista)

print(miTupla.count(13))"""

#desempaquetado de tuplas
"""miTupla = ("juan", 13, 1, 1995)
nombre, dia, mes, agno = miTupla
print("Nombre:" , nombre)
print("Dia:" , dia)
print("mes:" , mes)
print("año:" , agno)"""

#Diccionario
"""miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "reino unido":"Londres", "españa":"Madrid"}
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
miDiccionario["Italia"]="Roma"
print(miDiccionario)
del miDiccionario["reino unido"]
print(miDiccionario)"""

#miDiccionario = {"Alemania":"Berlin", 23:"veinti tres"}
"""miTupla = ["españa", "francia", "Reino unido", "alemania"]
miDiccionario = {miTupla[0]:"madrid", miTupla[1]:"Paris", miTupla[2]:"londres", miTupla[3]:"Berlin"}
print (miDiccionario)"""

#Combinacion de tuplas a listas y crear una clase:valor osea un diccionario
"""miDiccionario={23:"jordan", "nombre":"Michael", "equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario.keys())
print(miDiccionario.values())
print(len(miDiccionario))
print(miDiccionario["anillos"])"""

#Condicionales
"""print("Que nota sacaste en tu examen")
calificacion = input("Valor obtenido en examos: ")
def evaluacion(nota):
    Estado = "aprobado"
    if nota < 5:
        Estado = "suspenso"
    return Estado

print(evaluacion(int(calificacion)))"""

"""print("Verificacion de acceso")

edad_usuario=int(input("Introduce tu edad, por favor:"))

if edad_usuario < 18:
    print("no puedes pasar")
elif edad_usuario > 100:
    print("Ingresa una edad valida")
else:
    print("puedes pasar")

print("el programa ha finalizado")"""

#Ejercicio 1
"""num1 = int(input("Ingresa tu primer valor:"))
num2 = int(input("Ingresa tu segundo valor:"))

def DevuelveMax(n1, n2):
    if n1 > n2:
        print("El valor mas alto es:" , n1)
    elif n2 > n1:
        print("El valor mas alto es:", n2)
    else:
        print("Ingresa valores validos")

print(DevuelveMax(num1,num2))"""

#Ejercicio 2
"""nombre = input("Introduce tu nombre: ")
direccion = input("Introduce tu direccion: ")
tfno = int(input("Introduce tu numero telefonico: "))

Los_datos_personales_son = {"Datos personales":{"Los datos personales son:":[nombre, direccion, tfno]}}

print(Los_datos_personales_son["Datos personales"])"""

#Ejercicio 3
"""num1 = int(input("Introduce el primer numero: "))

num2 = int(input("Introduce el segundo numero: "))

num3 = int(input("Introduce el tercer numero: "))

media = (num1+num2+num3)/3

print("La Media aritmetica es:" , float(media))"""

#Bucles for variable in lo que recorra
"""for i in ["pildoras", "informaticas"]:
    print(i, end= " ")"""
#POO
"""class Coche():
    #propiedades

    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
    #comportamiento
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo = self.chequeo_interno()

        if(self.__enmarcha and chequeo):
            if(self.__enmarcha):
                return "El coche esta en marcha"
            elif(self.__enmarcha and chequeo == False):
                return "Algo ha ido mal en el chequeo. no podemos arrancar"
            else:
                return "El coche esta detenido"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "Ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def chequeo_interno(self):
        print("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


miCoche = Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("-------------------A continuacion creamos el segundo objeto-------------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()"""

#Herencia
"""class Vehiculos():

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

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

#heredacion
class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VehiculoElectrico(Vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

miMoto = Moto("honda", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(VehiculoElectrico, Vehiculos):
    pass

miBici = BicicletaElectrica("Orbea", "HC1030")

print("--------------------------------Otro POO--------------------------------------------------")

class persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):

        print("nombre:", self.nombre, " Edad:", self.edad, " Residencia:", self.lugar_residencia)

class empleado(persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario

        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()

        print("Salario:", self.salario, "Antiguedad:",self.antiguedad)

Manuel = persona("manuel", 55, "colombia")

Manuel.descripcion()

print(isinstance(Manuel, empleado))"""

#Polimorfismo
"""class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()

miVehiculo = Moto()

desplazamientoVehiculo(miVehiculo)"""

#Metodos de cadenas
"""nombreUsuario = input("introduce tu nombre de usuario:")

print("El nombre es: ", nombreUsuario.upper())

edad = input("Introduce la edad:")

while(edad.isdigit() == False):

    print("Por favor, introduce un valor numerico")

    edad= input("Introduce tu edad:")

if (int(edad) < 18):

    print("No puede pasar")
else:
    print("Puedes pasar")
#print(edad.isdigit())"""

#Ejercicio con metodo de cadena para encontrar fallas de correo electronico
"""correo = input("Introduce tu correo electronico:")

while correo.count("@") == 0 and correo.find("@")!= 0 and correo.find("@")!=len(correo)-1:
    correo = input("Ingresa un correo electronico valido:")
else:
    print("Tu correo electronico es correcto")"""

#Modulos en el archivo- funcione matematicas y uso de funciones



