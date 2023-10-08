correo=input("Escribe un correo: ")
contadorpunto=0
contadorarroba=0

for i in range(len(correo)):
	if correo[i]=="@":
		contadorarroba=contadorarroba+1
	if correo[i]==".":
		contadorpunto=1

if contadorarroba!=1 or contadorpunto==0:
	print("Correo inválido")
else:
	print("Correo válido") 