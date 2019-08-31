from Tkinter import *
from Tkinter import * 
import tkMessageBox
import Tkinter, Tkconstants, tkFileDialog
import tkMessageBox
import sqlite3
# from tkinter import messagebox

#----------------funciones------------------------

# Establecer conexion
def conexionBDD():

	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
				CREATE TABLE DATOS_USUARIOS(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				NOMBRE VARCHAR(50),
				PASSWORD VARCHAR(50),
				APELLIDOS VARCHAR(100),
				DIRECCION VARCHAR(50),
				COMENTARIOS VARCHAR(150))
			''')

		tkMessageBox.showinfo("BDD", "BDD creada con exito!!!")

	except:

		tkMessageBox.showwarning("Atencion","La BDD ya existe!!!")


# Salir de la aplicacion
def salirAplicacion():

	valor = tkMessageBox.askquestion("Salir","Deseas salir de la aplicacion")

	if valor=="yes":
		root.destroy()

# Resetear Campos
def limpiarCampos():

	miId.set("")
	miNombre.set("")
	miApellido.set("")
	miPass.set("")
	miDireccion.set("")
	textComentario.delete(1.0, END)

# Crear CRUD
def crearCRUD():

	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + miNombre.get() + 
		"','" + miPass.get() + 
		"','" + miApellido.get() +
		"','" + miDireccion.get() +
		"','" + textComentario.get("1.0", END) +
		"')")

	miConexion.commit()

	tkMessageBox.showinfo("BDD", "Registro insertado con exito!!!")

#-------------------------------------------------

root = Tk()

root.title("Practica guiada")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Establecemos cuantos elementos tendra nuestro menu principal
# tearoff = elimina la barra horizontal discontinua
bddMenu=Menu(barraMenu, tearoff=0)
borrarMenu=Menu(barraMenu, tearoff=0)
crudMenu=Menu(barraMenu, tearoff=0)
ayudaMenu=Menu(barraMenu, tearoff=0)

# Establecemos cual es el texto de los diferentes elementos del menu principal
barraMenu.add_cascade(label="BDD", menu=bddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# Creamos el submenu de BDD
bddMenu.add_command(label="Conectar", command=conexionBDD)
bddMenu.add_command(label="Salir", command=salirAplicacion)

# Creamos el submenu de Borrar
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

# Creamos el submenu de CRUD
crudMenu.add_command(label="Crear", command=crearCRUD)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

# Creamos el submenu de Ayuda
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


#-----------------------Comienzo de campos---------------------

miFrame = Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

# Input ID
cuadroId=Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

# Input Nombre
cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
# Texto de color rojo
#cuadroNombre.config(fg="red", justify="right")

# Input Apellidos
cuadroApellidos=Entry(miFrame, textvariable=miApellido)
cuadroApellidos.grid(row=2, column=1, padx=10, pady=10)

# Input Password
cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
# Texto con *
cuadroPass.config(show="*")

# Input Direccion
cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

# Textbox Comentarios
textComentario=Text(miFrame, width=16, height=5)
textComentario.grid(row=5, column=1, padx=10, pady=10)
# Creamos el Scroll vertical
scrollVert = Scrollbar(miFrame, command=textComentario.yview)
# Situamos el Scroll
scrollVert.grid(row=5, column=2, sticky="nsew")
textComentario.config(yscrollcommand=scrollVert.set)

#------------------------aqui comienzan los label--------------------

# Label ID
idLabel= Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

# Label Nombre
nombreLabel= Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

# Label Apellidos
apellidosLabel= Label(miFrame, text="Apellidos: ")
apellidosLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

# Label Password
passLabel= Label(miFrame, text="Password: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

# Label Direccion
direccionLabel= Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# Label Comentarios
direccionLabel= Label(miFrame, text="Comentarios: ")
direccionLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#----------------------aqui los botones------------------------------
miFrame2=Frame(root)
miFrame2.pack()

# Boton Crear
botonCrear=Button(miFrame2, text="Crear", command=crearCRUD)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

# Boton Leer
botonLeer=Button(miFrame2, text="Leer")
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

# Boton Actualizar
botonActualizar=Button(miFrame2, text="Actualizar")
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

# Boton Borrar
botonBorrar=Button(miFrame2, text="Borrar")
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()