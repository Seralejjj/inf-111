contador = 0
primos_por_linea = 10

print("Los números primos entre 2 y 1000 son:")
for num in range(2, 1001):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")
        contador += 1
        if contador % primos_por_linea == 0:
            print()
