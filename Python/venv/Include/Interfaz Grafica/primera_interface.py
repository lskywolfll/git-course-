from tkinter import *
#Mas informacion buscando standar library tkinter python
#cambiano el .py por pyw - para windows y asi no usara la terminal por detras
#ventana
raiz = Tk()
#caracteristicas
raiz.title("Ventana de pruebas")

#impedir que se redimencione el tamaño de la ventana
#raiz.resizable(0,0)
#para cambiar icono se teiene que agregar con imagen.ico
#raiz.iconbitmap("gato.ico") -Ejemplo
#para cambiar tamaño de la ventana por defecto
#raiz.geometry("650x350")
#Color de fondo
raiz.config(bg="blue")

raiz.config(bd = 45)
raiz.config(relief="groove")
raiz.config(cursor="hand2")

#frame - widgets y agregarlo a la raiz
miFrame = Frame()
#empaquetado ^^ y tambien se puede usar para establecerlo en un lugar en concreto
#miFrame.pack(side="right", anchor="s")
#miFrame.pack(fill="both", expand="True")
miFrame.pack()
#cambiar caracteristicas
miFrame.config(bg="red")
#Tener en cuenta las dimensiones con la cual se colorea
miFrame.config(width="650", height="350")
#antes de cambiar el borde necesitamos cambiar el borde
miFrame.config(bd = 35)
#caracteristicas del borde
miFrame.config(relief="sunken")
#Cambiar el cursor dentro del rango del frame
miFrame.config(cursor="pirate")


#es necesario un bucle infinito para que la aplicacion este siempre activa y siempre esta al final
raiz.mainloop()

