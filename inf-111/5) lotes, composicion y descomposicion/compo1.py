numero = int(input(""))

positivos = 0
negativos = 0
suma_total = 0
contador = 0 

while numero != 0:
    if numero > 0:
        positivos += 1 
    elif numero < 0:
        negativos += 1

    suma_total += numero
    contador += 1

    numero = int(input())

if contador > 0:
    promedio = suma_total / contador
else:
    promedio = 0.0
print("El número de positivos es", positivos)
print("La cantidad de negativos es", negativos)
print("La suma total es", float(suma_total)) 
print("El promedio es", promedio)