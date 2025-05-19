# inicio
n1 = float(input("Ingrese n1: "))
n2 = float(input("Ingrese n2: "))
n3 = float(input("Ingrese n3: "))
n4 = float(input("Ingrese n4: "))
n5 = float(input("Ingrese n5: "))

# proceso
minimo = n1
maximo = n1

# Determinar el mínimo
if n2 < minimo:
    minimo = n2
if n3 < minimo:
    minimo = n3
if n4 < minimo:
    minimo = n4
if n5 < minimo:
    minimo = n5

# Determinar el máximo
if n2 > maximo:
    maximo = n2
if n3 > maximo:
    maximo = n3
if n4 > maximo:
    maximo = n4
if n5 > maximo:
    maximo = n5

# imprimir
print("Resultado: Mínimo =", minimo, ", Máximo =", maximo)
