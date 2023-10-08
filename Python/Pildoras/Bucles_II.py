#print ('Para que todo lo que imprima el bucle sea en una línea ( ,end="") ')

print ("Programa para evaluar si tu email es correcto.")

contador=0
email=input("Escribe tu email: ")
for i in email:
	if i=="@" or i==".":
		contador=contador+1

if contador>=2:
	print ("Tu email es correcto\n")
else: 
	print("Tu email es incorrecto\n")