def insercion(V, n):
    for i in range(1, n):
        key = V[i]
        j = i - 1
        while j >= 0 and V[j] > key:
            V[j + 1] = V[j]
            j -= 1
        V[j + 1] = key

n = int(input("n: "))
A = [0] * n

def leeVector(V, n):
    for i in range(n):
        V[i] = int(input("x: "))

leeVector(A, n)
insercion(A, n)
print("Vector ordenado (inserción):", A)