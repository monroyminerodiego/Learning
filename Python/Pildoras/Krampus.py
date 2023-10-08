print ("                                                Krampus.\n")

def login ():
	nombre=input("Por favor, ingresa tu nombre: ")
	apellido_paterno=input("\nPor favor, ingresa tu apellido paterno: ")

	correo=input("\nPor favor, ingresa tu correo electronico: ")
	validacióncorreo=False
	contadorarroba=0
	contadorpunto=0
	while validacióncorreo==False:
		for i in correo:
			if i=="@":
				contadorarroba+=1
			if i==".":
				contadorpunto=1

		if contadorpunto==1 and contadorarroba==1:
			validacioncorreo=True
			break

	contraseña=input("\nEscribe una contraseña de mínimo 8 dígitos sin espacio: ")
	validacioncontraseña=True
	for i in contraseña:
		while len(contraseña)<8 or i==" ":
			validacioncontraseña=False
			print("Contraseña inválida.")
			contraseña=input("\nEscribe una contraseña de mínimo 8 dígitos sin espacio: ")

crear=input("¿Ya tienes un usuario?: ")
crear=crear.lower()
if crear=="no":
	login()
elif crear=="si" or crear=="sí":
	pass

cerrar=input("Presiona 'Enter' para cerrar el programa")