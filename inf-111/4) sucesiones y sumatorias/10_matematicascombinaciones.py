numeros = [1, 2, 3, 4, 5, 6, 7]

total = 0

print("Combinaciones posibles:")

for primero in numeros:

    for segundo in numeros:
        if segundo > primero:
            print(primero, segundo)
            total += 1

print("\nTotal de combinaciones:", total)