#Funciones continue, pass y else.

#print("Contador de letras de un nombre.\n")
#nombre=input("Escribe tu nombre: ")
#contador=0
#for i in nombre:
#	if i==" ":
#		continue
#	contador+=1
#print("Tu nombre tiene",contador,"letras.")

#pass sólo sirve para hacer que la línea de código salte
#while True:
#	pass

email=input("Escribe tu correo: ")
for i in email:
	if i=="@":
		arroba=True
		break;
	
else:
	arroba=False

print(arroba)