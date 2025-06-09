def seleccion(V, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if V[j] < V[min_idx]:
                min_idx = j
        V[i], V[min_idx] = V[min_idx], V[i]

n = int(input("n: "))
A = [0] * n

def leeVector(V, n):
    for i in range(n):
        V[i] = int(input("x: "))

leeVector(A, n)
seleccion(A, n)
print("Vector ordenado (selección):", A)