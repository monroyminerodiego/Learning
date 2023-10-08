print ("UNA MISMA VARIABLE.")
mensaje = "Hola"
mensaje += ","
mensaje += " Diego"
print (mensaje)
print (" ")
print ("CONCATENACIÓN.")
espacio = " "
apellido = "Monroy"
print (mensaje+espacio+apellido)
print (" ")
print ("EJEMPLO NUMERO Y TEXTO.")
numero1 = 95
numero2 = 5
resultado = numero1+numero2
resultado = str (resultado)
print ("El resultado de ",numero1,"+",numero2,"es:",resultado)
print (" ")
print ("BUSCAR.")
buscar_subcadena = mensaje.find("Diego")
print (buscar_subcadena)
print ("")
print ("EXTRACCIÓN.")
extraer_subcadena = mensaje[6:12]
print (extraer_subcadena)
print ("")
print ("COMPARACIÓN.")
mensaje1 = "Diego"
mensaje2 = "Monroy"
print (mensaje1 == mensaje2)
