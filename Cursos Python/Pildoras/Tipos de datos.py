print ("Tipos de datos.")
print ("Los tipos de datos son:")
print ("""- Enteros y largos.
- Flotantes.
- Números complejos.
- Cadenas.
- Booleanos.""")

print ("")
print ("Enteros y Largos:")
print ("""Enteros = que no tiene decimales.
Se representa mediante 'int', que es entero o el tipo largo 'long'.""")
print ("Ejemplo:")
numero = 15
print(numero, type(numero))

print ("")
print ("Flotantes o Reales:")
print ("""Son los que tienen decimales.
Se representan con 'float'.""")
print ("Ejemplo:")
numero = 15.5
print(numero, type(numero))

print ("")
print ("Numeros complejos:")
print ("""Tienen una parte real y una parte imaginaria.
Se representa mediante 'complex'.""")
print ("Ejemplo:")
numero = 5 + 5j
print (numero, type (numero))

print ("")
print ("Cadenas:")
print ("Son conocidas como strings")
print ("Ejemplo:")
nombre = "Diego"
print (nombre, type (nombre))

print ("")
print ("Booleanos:")
print ("""sólo hay dos valores, 'true' y 'false'.
Son importantes para expresiones condicionales y los bucles.
Se expresa como 'bool'.""")
print ("Ejemplo:")
true_false = 3 == 3
print (true_false, type (true_false))
