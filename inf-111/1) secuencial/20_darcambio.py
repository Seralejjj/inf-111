import math
# inicio
pago = float(input("Ingrese numero pago: "))
total_venta = float(input("Ingrese total venta: "))
# Proceso
cambio = pago - total_venta

monedas_5 = cambio // 5
monedas_2 = cambio // 2
monedas_1 = cambio // 1
monedas_50 = cambio // 0.50
monedas_20 = cambio // 0.25
monedas_10 = cambio // 0.10
# Imprimir
print("Resultado: ", monedas_5, monedas_2, monedas_1, monedas_10, monedas_20, monedas_50)