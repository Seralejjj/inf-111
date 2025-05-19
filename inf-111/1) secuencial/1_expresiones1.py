import math
# inicio
T = float(input("INGRESE T: "))
# Proceso
a = 56 * T - 9.81 * (T ** 2 / 2)
b = 14 * math.exp(-0.1 * T) * math.sin(2 * math.pi * T)
# Imprimir
print("Resultado: ", a, b)
