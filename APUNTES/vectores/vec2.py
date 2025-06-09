def leeVector(V, n):
    for i in range(n):
        V[i] = int(input("x: "))

def maximo(V, n):
    aux = V[0]
    pos = 0
    for i in range(1, n):
        if V[i] > aux:
            aux = V[i]
            pos = i
    return aux, pos

def minimo(V, n):
    aux = V[0]
    pos = 0
    for i in range(1, n):
        if V[i] < aux:
            aux = V[i]
            pos = i
    return aux, pos

n = int(input("n: "))
A = [0] * n
leeVector(A, n)

mayor, pos_max = maximo(A, n)
menor, pos_min = minimo(A, n)

print("Máximo =", mayor)
print("Posición del máximo =", pos_max)
print("Mínimo =", menor)
print("Posición del mínimo =", pos_min)
