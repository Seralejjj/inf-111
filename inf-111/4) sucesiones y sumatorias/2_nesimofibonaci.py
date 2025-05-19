n = int(input("Ingrese el valor de n: "))
a = 0
b = 1
contador = 2

while contador <= n:
    c = a + b
    print(c, end=" ")
    a, b = b, c
    contador += 1

print(a, b, end=" ")