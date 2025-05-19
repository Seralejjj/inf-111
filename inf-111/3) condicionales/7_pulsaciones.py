import math

sexo = int(input("Ingrese el sexo (1 para masculino, 2 para femenino): "))
edad = float(input("Ingrese la edad: "))

pulsaciones = 0

if sexo == 1:
    pulsaciones = (220 - edad) / 10
elif sexo == 2:
    pulsaciones = (210 - edad) / 10
else:
    print("Fuera de rango")

print("Pulsaciones:", pulsaciones)
