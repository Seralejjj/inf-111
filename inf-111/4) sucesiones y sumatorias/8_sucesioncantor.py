n = int(input("Ingrese el valor de n: "))

k = 1
while n > k * (k + 1) // 2:
    k += 1

pos = n - k * (k - 1) // 2

if k % 2 == 0:
    numerador = pos
    denominador = k - pos + 1
else:
    numerador = k - pos + 1
    denominador = pos

print(f"{numerador}/{denominador}")