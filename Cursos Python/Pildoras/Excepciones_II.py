def divide ():
	
	try: #Siempre va con un finally o un except
		op1=float(input("Introduce el primer valor: "))
		op2=float(input("Introduce el segundo valor: "))
		print ("La división es: "+str(op1/op2))
	except ZeroDivisionError:
		print("No se puede divir entre 0.")
	except ValueError:
		print("No se admiten letras.")
	
	finally: #Esto siempre se ejecuta
	print ("\nCálculo finalizado")

divide()