import math
def raíz(num1):
	if num1<0:
		raise ValueError ("El número no puede ser negativo.")

	else:
		return math.sqrt (num1) 

num1=int(input("introduce un número: "))

try:
	print(raíz(num1))
except ValueError as Errornumeronegativo:
	print (Errornumeronegativo)

input("\nPresiona enter para finalizar el programa")