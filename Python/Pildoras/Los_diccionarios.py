print ("Estructura de un diccionario.")
diccionario1={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","México":"CdMx"}
print("")
print (diccionario1)

print("\nConocer un valor de un diccionario escribiendo la clave:")
print(diccionario1["México"])

print ("\nCómo agregar un valor a un diccionario:")
diccionario1["España"]="Marruecos"
print (diccionario1)
print("\nPara corregir un valor en un diccionario:")
diccionario1["España"]="Madrid"
print(diccionario1)

print("\nPara eliminar un elemento de un diccionario (del):")
del diccionario1["España"]
print(diccionario1)

print("\nPara dar los datos de una tupla a un diccionario:")
tupla1=["España","Francia","Reino Unido","Alemania"]
print(tupla1)
diccionario2={tupla1[0]:"Madrid",tupla1[1]:"Paris",tupla1[2]:"Londres",tupla1[3]:"Berlín"}
print (diccionario2["Francia"])

print("\nQue el diccionario guarde una tupla:")
diccionario3={"Nombre":"Diego","Apellidos":{"Materno":["Minero"],"Paterno": ["Monroy"]} }
print (diccionario3)

print("\nPara devolver las claves de un diccionario (.keys):")
print(diccionario1.keys())

print("\nPara devolver los valores de un diccionario (.values):")
print(diccionario1.values())

print("\nPara devolver la longitud de un diccionario (len):")
print(len(diccionario1))