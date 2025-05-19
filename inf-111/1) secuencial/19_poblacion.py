import math
# inicio
años = float(input("Ingrese años: "))
# Proceso
segundos = 365*24*60*60

nacimiento = (segundos * años) / 7
muertos = (segundos * años) / 13
inmigrantes = (segundos * años) / 45

futuro = nacimiento - muertos + inmigrantes
# Imprimir
print("Resultado: ", futuro)