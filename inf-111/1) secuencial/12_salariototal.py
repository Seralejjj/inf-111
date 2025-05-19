import math
# inicio
horas_extras = float(input("Ingrese horas extras: "))
sal_hora = float(input("Ingrese salario hora: "))
horas_regular = float(input("Ingrese hora regular: "))
# Proceso
sal_regular = sal_hora * horas_regular
sal_extra = horas_extras * sal_hora
t = sal_regular + sal_extra
# Imprimir
print("Resultado: ", t)

