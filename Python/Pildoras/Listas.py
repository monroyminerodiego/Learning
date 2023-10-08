lista1 = ["Javier", "Diego","Eduardo","Clau"]
print ("Primer lista:",lista1)
print ("Elemento 0:",lista1[0])
print ("Elemento -2:",lista1[-2])
print ("Del elemento 0 al 3:",lista1[0:3])
print ("Del cero al 3:",lista1[:3])
print ("Del 3 al final:",lista1[3:])
lista1.append(input("Agrega un nuevo nombre al final: "))
print (lista1[:])

lista1.insert(int(input("Agrega el indice donde lo agregaras: ")),input("Agrega el elemento: "))
print(lista1[:])

lista1.extend(["Karen","Fer"])
print (lista1[:])

print(lista1.index("Diego"))

print ("Diego" in lista1)

lista1.remove (input("Escribe el elemento que quieres eliminar: "))
print("Lista actualizada: ",lista1[:])

lista1.pop()
print (lista1[:])

lista2 = ["Karen","Fer","Alfredo"]
print ("Segunda lista:",lista2[:])

lista3=lista1+lista2
print("Suma de las 2 listas:",lista3[:])

print("Segunda lista repetida 3 veces:")
print (lista2[:]*3)

input ("\nPresiona enter para cerrar el programa:")