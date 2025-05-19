import math

h1 = float(input("Ingrese h1: "))
m1 = float(input("Ingrese m1: "))
h2 = float(input("Ingrese h2: "))
m2 = float(input("Ingrese m2: "))

# Convertir horas a minutos
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

# Calcular la diferencia
dif = t2 - t1

# Asegurarse de que la diferencia sea positiva
if dif < 0:
    dif = -dif  

horas = dif // 60
minutos = dif % 60  

print("Diferencia: {} horas y {} minutos".format(horas, minutos))
