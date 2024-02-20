# Operaciones matematicas entre 2 numeros

import os; os.system("clear")

print("Realizando operaciones matematicas entre 2 numeros floatantes\n")

x = float(input("Dame el valor de x : "))
y = float(input("Dame el valor de y : "))

suma = x + y
resta = x - y
mult = x * y 
div = x / y
res = x % y
exp = x ** y
dive = x // y

print("\nResultado de las operaciones:\n")
print(f"suma:{suma}\nresta:{resta}\nmultiplicacion:{mult}\ndivision:{div}\nresiduo:{res}\nexponenciacion:{exp}\ndivision entera:{dive}")