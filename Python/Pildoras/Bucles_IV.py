#print("Programa para evaluar tu edad.")
#edad=int(input("Introduce tu edad: "))

#while edad<5  or edad>99:
	#print ("Introdujiste una opción inválida.")
	#edad=int(input("Introduce tu edad: "))

#print ("\nIntrodujiste una opción válida")

import math
print ("Programa para conocer la raíz cuadrada de un número.")
numero=int(input("Escribe un número: "))
intentos=0

while numero < 0:
	print("\nNo se puede hallar la raíz cuadrada de un número negativo.")

	if intentos==2:
		print("Has consumido muchos intentos.")
		break; #Break para salir del bucle

	numero=int(input("Escribe un número: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solución= math.sqrt(numero)
	print("\nLa raíz cuadrada de "+str(numero)+" es "+str(solución))