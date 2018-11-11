from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width = 1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1,column=4)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=4)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=4)

nombreLabel=Label(miFrame,text="Nombre")
nombreLabel.grid(row=1,column=3)

ApellidoLabel=Label(miFrame,text="Apellido")
ApellidoLabel.grid(row=2,column=3)

DireccionLabel=Label(miFrame,text="Direccion de casa")
DireccionLabel.grid(row=3,column=3)

raiz.mainloop()


print("hola")
