print ("======================================")
print ("Sistema de control de vacaciones Rappi.")
print ("======================================")
nombre = input ("\nHola, por favor escribe tu nombre: ")
clave = input ("\n"+nombre+", por favor escribe tu clave de departamento [Atención a Clientes (AC), Logística (L) y Gerencia (G)]: ")
clave = clave.lower()
if clave == "ac":
    antiguedad = input ("\n"+nombre+", por favor escribe tu antigüedad (Únicamente los años): ")
    if antiguedad < "1":
        print ("\n",nombre,"no tienes derecho a vacaciones.")
    elif antiguedad >= "1" and antiguedad < "2":
        print ("\n",nombre,"tienes derecho a 6 días de vacaciones.")
    elif antiguedad >= "2" and antiguedad <= "6":
        print ("\n",nombre,"tienes derecho a 14 días de vacaciones.")
    elif antiguedad >= "7":
        print ("\n",nombre,"tienes derecho a 20 días de vacaciones.")
    else:
        print ("\nFormato de año incorrecto.")
elif clave == "l":
    antiguedad = int(input ("\n"+nombre+", por favor escribe tu antigüedad (Únicamente los años): "))
    if antiguedad < "1":
        print ("\n",nombre,"no tienes derecho a vacaciones.")
    elif antiguedad >= "1" and antiguedad < "2":
        print ("\n",nombre,"tienes derecho a 7 días de vacaciones.")
    elif antiguedad >= "2" and antiguedad <= "6":
        print ("\n",nombre,"tienes derecho a 15 días de vacaciones.")
    elif antiguedad >= "7":
        print ("\n",nombre,"tienes derecho a 22 días de vacaciones.")
    else:
        print ("\nFormato de año incorrecto.")
elif clave == "g":
    antiguedad = int(input ("\n"+nombre+", por favor escribe tu antigüedad (Únicamente los años): "))
    if antiguedad < "1":
        print ("\n",nombre,"no tienes derecho a vacaciones.")
    elif antiguedad >= "1" and antiguedad < "2":
        print ("\n",nombre,"tienes derecho a 10 días de vacaciones.")
    elif antiguedad >= "2" and antiguedad <= "6":
        print ("\n",nombre,"tienes derecho a 20 días de vacaciones.")
    elif antiguedad >= "7":
        print ("\n",nombre,"tienes derecho a 30 días de vacaciones.")
    else:
        print ("\nFormato de año incorrecto.")
else:
    print ("\nClave no válida.")
