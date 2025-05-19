numeros = []
print("Ingrese diez números separados por espacios:")
entrada = input().split() 

for num in entrada:
    numeros.append(float(num))

suma = sum(numeros)
n = len(numeros)
media = suma / n

suma_cuadrados = 0
for num in numeros:
    suma_cuadrados += (num - media) ** 2  

desviacion = (suma_cuadrados / n) ** 0.5  

print(f"La media es {media:.2f}")
print(f"La desviación estándar es {desviacion:.5f}")