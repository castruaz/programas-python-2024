# Leer datos y enviar un saludo

print('Leyendo datos y enviando un saludo: \n')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame la edad: '))
peso = float(input('Dame tu peso: '))

print('Tu nombre es ' + nombre + " tu edad es " + str(edad) + " tu peso es " + str(peso))
print('Tu nombre es',nombre,'tu edad es',edad,'tu peso es',peso)
print(f'Tu nombre es {nombre}, tu edad es {edad}, tu peso es {peso}')

alerta = peso > 65

print(alerta)

print(type(nombre))
print(type(edad))
print(type(peso))
print(type(alerta))
