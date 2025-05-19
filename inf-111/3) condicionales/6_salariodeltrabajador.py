import math

horas = float(input("Ingrese horas trabajadas: "))
salario = float(input("Ingrese salario por hora: "))

if horas < 40:
    salario_total = horas * salario
else:
    normales = 40
    h_extras = horas - 40
    sal_extra = h_extras * (salario * 1.5)
    salario_total = (normales * salario) + sal_extra

print("Salario total:", salario_total)
