print ("=========")
print ("Conversor")
print ("=========\n")
print ("Menú de opciones:\n")
print ("Presiona 1 para convertir de número a letra.")
print ("presiona 2 para convertir de letra a número.\n")
opcion = input ("¿Cuál es la opción deseada?: ")
if opcion == "1":
    print ("                Convertidor de número a letra.")
    num_letra = input ("¿Cuál es el número que deseas convertir?: \n")
    if num_letra == "0":
        print ("El número es 'Cero'")
    elif num_letra == "1":
        print ("El número es 'Uno'")
    elif num_letra == "2":
        print ("El número es 'Dos'")
    elif num_letra == "3":
        print ("El número es 'Tres'")
    elif num_letra == "4":
        print ("El número es 'Cuatro'")
    elif num_letra == "5":
        print ("El número es 'Cinco'")
    else:
        print ("opción no válida.")
elif opcion == "2":
    print ("                Convertidor de letra a número.\n")
    letra_num = input ("¿Cuál es el número que deseas convertir?: \n")
    letra_num = letra_num.lower()
    if letra_num == "cero":
        print ("El número es '0'")
    elif letra_num == "uno":
        print ("El número es '1'")
    elif letra_num == "dos":
        print ("El número es '2'")
    elif letra_num == "tres":
        print ("El número es '3'")
    elif letra_num == "cuatro":
        print ("El número es '4'")
    elif letra_num == "cinco":
        print ("El número es '5'")
    else:
        print ("opción no válida.")
else:
    print ("Opción no valida.")
print ("Fin.")
