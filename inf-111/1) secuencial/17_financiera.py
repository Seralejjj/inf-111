import math
# inicio
total = float(input("Ingrese total: "))
porcentaje = float(input("Ingrese porcentaje: "))
# Proceso
propina = total * (porcentaje / 100)
pagar = total + propina
# Imprimir
print("Resultado: ", propina, pagar)

