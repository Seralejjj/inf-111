def leeVector(V, n):
    for i in range(n):
        V[i] = int(input("x: "))

def suma_pares(V, n):
    suma = 0
    for i in range(n):
        if V[i] % 2 == 0: #if V[i] % 2 != 0:
            suma += V[i]
    return suma

n = int(input("n: "))
A = [0] * n
leeVector(A, n)

sumaPares = suma_pares(A, n)
print("Suma de pares =", sumaPares)
