# Verificar si la suma de dos numeros es igual a un tercero

import os; os.system("clear")

print("Verificando si la suma de dos numeros es igual a un tercero :\n")

print("Dame 3 numeros enteros, separados por <Enter>:")

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3 :
    print("Son Iguales")
else:
    print("Son Distintos")

print("Proceso terminado")
