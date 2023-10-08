nombre = input ("¿Cuál es tu nombre?: ")
quimica = float (input ("Hola "+nombre+", ¿Cuánto sacaste en química?:"))
matematicas = float (input ("¿Y en matemáticas?: "))
biologia = float (input ("Por último "+nombre+", ¿Cuánto sacaste en biología?: "))
promedio = (quimica+matematicas+biologia)/3
print ("Tu promedio es de: ",int (promedio))
if promedio >= 6:
    print ("¡Felicidades!, pasaste de año.")
if promedio < 6:
    print ("¡Rayos!, no pasaste de año.")
