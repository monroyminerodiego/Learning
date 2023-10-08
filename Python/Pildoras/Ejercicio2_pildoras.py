contraseña=input("Escribe una contraseña: ")
contador=0

for i in contraseña:
	if i==" ":
		contador=contador+1
if len(contraseña)<8 or contador>0:
	print("Contraseña no válida")
else:
	print("Contraseña válida")