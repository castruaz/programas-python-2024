# Aceptar un estudiante en base a la edad y dos calificaciones

import os; os.system("clear")

print("Universidad patito SA de CV")
print("Validacion de inscripcion \n")

nombre = input("Dame tu nombre ? ")
edad   = int(input("Dame tu edad ? "))

if edad<18:
    print("\nSolo aceptamos estudiantes mayores de edad")
else:
    print("Dame 2 calificaciones separados por <Enter>:")
    c1, c2 = int(input()), int(input())
    if c1<8 or c2<8:
        print("\nSolo aceptamos estudiantes con calificaciones mayores a 8")
    else:
        print(f"{nombre}, bienvenid@ a la Universidad Patito, tu edad {edad} y tus calificaciones {c1}, {c2} lo permiten")


print("\nProceso terminado")
