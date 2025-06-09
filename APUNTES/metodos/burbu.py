def burbuja(V, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if V[j] > V[j + 1]:
                V[j], V[j + 1] = V[j + 1], V[j]

n = int(input("n: "))
A = [0] * n

def leeVector(V, n):
    for i in range(n):
        V[i] = int(input("x: "))

leeVector(A, n)
burbuja(A, n)
print("Vector ordenado (burbuja):", A)