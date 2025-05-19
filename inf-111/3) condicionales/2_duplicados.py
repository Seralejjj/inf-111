# inicio
n1 = float(input("Ingrese n1: "))
n2 = float(input("Ingrese n2: "))
n3 = float(input("Ingrese n3: "))
n4 = float(input("Ingrese n4: "))
n5 = float(input("Ingrese n5: "))

# proceso
if n1 == n2 or n1 == n3 or n1 == n4 or n1 == n5:
    hay = "dublicados"
if n2 == n3 or n2 == n4 or n2 == n5:
    hay = "dublicados"
if n3 == n4 or n3 == n5:
    hay = "dublicados"
if n4 == n5:
    hay = "dublicados"
# imprimir
print("En aqui hay: ", hay)
