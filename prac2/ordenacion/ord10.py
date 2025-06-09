def leer():
    n = int(input())
    v = list(map(int, input().split()))
    a, b = map(int, input().split())
    return v, a, b

def buscar(v, x):
    for i in range(len(v)):
        if v[i] == x:
            return i+1
    return 0

def buscar_cercano(v, x):
    cercano = v[0]
    dif = abs(x - v[0])
    for num in v:
        if abs(x - num) < dif:
            dif = abs(x - num)
            cercano = num
    for i in range(len(v)):
        if v[i] == cercano:
            return i+1, cercano

def ordenar(v):
    for i in range(len(v)):
        for j in range(len(v)-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]

# Programa principal
v, a, b = leer()
p1 = buscar(v, a)
p2 = buscar(v, b)
suma = p1 + p2

pos, val = buscar_cercano(v, suma)
ordenar(v)

print(' '.join(map(str, v)))
if p1 > 0: print(f"{p1}:{v[p1-1]}", end=' ')
if p2 > 0: print(f"{p2}:{v[p2-1]}")
if suma > 0: print(f"{pos}:{val}")