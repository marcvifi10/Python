class Vehiculos():
	
	# Constructor con parametros
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

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

	def descripcion(self):
		print("-----VEHICULO-----","\nMarca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

# Creamos la clase Moto, que hereda de la clase Vehiculos
class Moto(Vehiculos):
	hcaballito = ""

	def caballito(self):
		self.hcaballito = "Voy haciendo el caballito!!!"

	# Para sobreescribir un metodo heredado, solo hace falta volverlo a escribir en la clase heredada
	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena,"\n",self.hcaballito)

# Creamos una clase Furgoneta, que hereda de la clase Vehiculos
class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado = cargar

		if(self.cargado):
			return "La furgoneta esta cargada"

		else:
			return "La furgoneta no esta cargada"

# Creamos una clase VElectricos
class VElectricos(Vehiculos):
	def __init__(self, autonomia, marca, modelo):

		# Llamamos al constructor de la clase padre
		super().__init__(marca,modelo)

		self.autonomia = autonomia

	def cargarEnergia(self):
		self.cargando = True

	def descripcion(self):

		# Llamamos al metodo descripcion de la clase padre, con la palabra super()
		super().descripcion()

		print("Autonomia:",self.autonomia)

# Creamos una clase BicicletaElectrica, que hereda de las clases VElectricos y Vehiculos
class BicicletaElectrica(VElectricos,Vehiculos):
	pass