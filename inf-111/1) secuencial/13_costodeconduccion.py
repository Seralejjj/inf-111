import math
# inicio
distancia = float(input("Ingrese distancia: "))
litro = float(input("Ingrese litro: "))
precio = float(input("Ingrese hora precio: "))
# Proceso
litros = distancia / litro
costo = (litros * precio)
# Imprimir
print("Resultado: ", costo)

