print ("    CONJUNCIÓN (and).\n")
num1 = int (input ("Escribe un número mayor a 2 y menor a 5: "))
if num1 > 2 and num1 < 5:
    print ("El número",num1,"cumple la condición. \n")
else:
    print ("El número",num1,"no cumple la condición.\n")
print ("    DISYUNCIÓN (or). \n")
palabra = input("Para cumplir con la condición, escribe 'SI' o 'YES'")
palabra = palabra.lower()
if palabra == "si" or palabra == "yes":
    print ("La condición se cumplió.")
else:
    print ("La condición no se cumplió.")
print ("\n    NEGACIÓN (not).\n")
numero1 = input ("introduce un número igual a 5: ")
if not numero1 == "5":
    print ("\nEl número no es igual a 5 y si se cumple la condición.")
else:
    print ("\nEl número es igual a cinco y no se cumple la condición.")
