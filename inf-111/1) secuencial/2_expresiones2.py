import math
# inicio
x = float(input("INGRESE x: "))
y = float(input("INGRESE y: "))
# Proceso
a = (3 / 4) * x * y - (7 * x) / (y ** 2) + math.sqrt(x + y)
b = (x * y) ** 2 - (x + y) / (x - y) ** 2 + math.sqrt((x + y) / (2 * x - y))
# Imprimir
print("Resultado: ", a, b)