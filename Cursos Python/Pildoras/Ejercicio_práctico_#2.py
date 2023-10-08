print ("******************************************************")
print ("* Programa que determina si un número es par o impar *")
print ("******************************************************\n")
numero = int(input("Por favor, introduce un número entero (sin decimales): "))
resultado = numero%2
if resultado == 0:
    print ("El número ",numero," es par.")
else:
    print ("El número ",numero," es impar.")
