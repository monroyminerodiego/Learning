print ("Sistema para calcular el promedio de un alumno.")
nombre = input ("Para comenzar, ¿Cuál es tu nombre?: ")
mate = float(input (nombre+" ¿Cuánto sacaste en Matemáticas?: "))
quim = float(input (nombre+" ¿Cuánto sacaste en Química?: "))
bio = float(input (nombre+" ¿Cuánto sacaste en Biología?: "))
promedio = (quim+mate+bio)/3
if promedio >= 6:
    print ("¡Felicidades,",nombre+"!, pasaste con promedio de:",round (promedio,2))
else:
    print ("¡Rayos,",nombre+"!, reprobaste con promedio de:",round (promedio,2))
