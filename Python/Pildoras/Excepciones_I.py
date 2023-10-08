def sumar(num1,num2):
	return num1+num2
def restar(num1,num2):
	return num1-num2
def multiplicar(num1,num2):
	return num1*num2
def dividir(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre cero.")
		return "Operación erronea"

while True:
	try:
		op1=int(input("Escribe un número: "))
		break
	except ValueError:
		print("El Valor introducido no es válido.\n")
while True:
	try:
		op2=int(input("Escribe un segundo número: "))
		break
	except ValueError:
		print("El Valor introducido no es válido.\n")

operación=input("\n¿Qué operación deseas realizar? (Sumar/Restar/Multiplicar/Dividir): ")
operación=operación.lower()

if operación=="sumar":
	print ("\nEl resultado de la suma de los dos números es:",sumar(op1,op2))

elif operación=="restar":
	print ("\nEl resultado de la resta de los dos números es:",restar(op1,op2))

elif operación=="multiplicar":
	print ("\nEl resultado de la multiplicación de los dos números es:",multiplicar(op1,op2))

elif operación=="dividir":
	print ("\nEl resultado de la división de los dos números es:",dividir(op1,op2))

else:
	print ("\nIntrodujiste una opción no contemplada")

print("Operación contemplada. Continuar con el código.")

input=("\nPresiona 'Enter' para cerrar e programa.")