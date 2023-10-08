#Utilidad del 'range':
print("Dentro del parametro del 'range' se pone ('desde donde empieza','hasta donde termina','de cuanto en cuanto')")
for i in range(5,50,5):
	print (f"valor de la variable {i}")

#Utilidad del 'len':
valido=False
email=input("\nIntroduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True
if valido:
	print("El email es correcto")
else:
	print("El email esta incorrecto")