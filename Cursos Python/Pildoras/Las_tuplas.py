print("									TUPLAS Y LISTAS\n")

tupla1=("Diego", 25,3,2002)
tupla2=("Diego",)
print(tupla1)
print(tupla2)

print ("\nPara convertir de tupla a lista (list):")
lista1=list(tupla1)
print ("Lista [Corchetes]:",lista1[:])

print("\nPara convertir de lista a tupla (tuple):")
tupla1=tuple(lista1)
print ("Tupla (Paréntesis):",tupla1[:])

print("\nSaber si hay un elemento en una tupla (in):")
print ("Diego" in tupla1)

print("\nContar cuantas veces esta un elemento (count):")
print(tupla1.count(25))

print("\nSaber cuantos elementos hay en una tupla (len):")
print(len(tupla1))
print ("Poner coma a la tupla para que la cuente como una tupla unitaria.")
print(len(tupla2))

print("\nAsignar elemetos de una tupla a una varible (Desempaquetado de tuplas):")
nombre, dia, mes, anio=tupla1
print(nombre, dia, anio, mes)

print("\n'Desempaquetar tuplas' también sirve con las listas:")
prueba=["Diego",25,3,2002]
name,day,month,year=prueba
print (name,day,month,year)

input ("\nPresiona 'Enter' para cerrar el programa.")