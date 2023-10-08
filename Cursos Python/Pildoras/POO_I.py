#Primera letra de la clase en mayúscula.
class Coches():
	#Método constructor
	def __init__(self):

		#Propiedades
		self.largochasis=250
		self.anchochasis=120
		#Para encapsular una propiedad se ocupan dos guines bajos.
		self.__ruedas=4
		self.enmarcha=False

	#Para crear un método (comportamiento) es "def"
	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos
		if (self.enmarcha):
			return "El coche está en marcha."
		else:
			return "El coche está parado."

	def estado(self):
		print("El coche tiene",self.__ruedas,"ruedas. Un ancho de chasis de",self.anchochasis,
			"cm, y un largo de chasis de",self.largochasis,"cm.")

#Instanciar una clase
miCoche=Coches()

print(miCoche.arrancar(True))
miCoche.estado()

print("\n----------A continuación creamos el segundo coche.----------\n")

miCoche2=Coches()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()
