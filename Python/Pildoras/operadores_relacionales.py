print ("COMPARADOR DE NÚMEROS.\n")

num1 = input ("Intorduce el primer número: ")
num2 = input ("introduce el segundo número: ")

print ("\n    Los números a comparar son:",num1,"y",num2,"\n")

if num1 == num2:
    print ("El "+num1+" es igual que "+num2+"...")
if num1 < num2:
    print ("El "+num1+" es menor que "+num2+"...")
if num1 > num2:
    print ("El "+num1+" es mayor que "+num2+"...")
if num1 != num2:
    print ("El "+num1+" es diferente que "+num2+"...")
if num1 <= num2:
    print ("El "+num1+" es menor o igual que "+num2+"...")
if num1 >= num2:
    print ("El "+num1+" es mayor o igual que "+num2+"...")
print ("Fin.")
