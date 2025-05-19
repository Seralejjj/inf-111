import math 

n = float(input("Ingrese n: "))

# Inicializar variables
unidades = 0
decenas = 0
especiales = ["Diez", "Once", "Doce", "Trece", "Catorce", "Quince", "Dieciséis", "Diecisiete", "Dieciocho", "Diecinueve"]

if n < 10:
    unidades = n  
elif 10 <= n <= 19:
    print("Número especial:", especiales[int(n - 10)])  # Imprimir el número especial
else:
    d = n // 10  # Decenas
    u = n % 10   # Unidades
    decenas = d
    unidades = u

print("Decenas:", decenas, "Unidades:", unidades)
