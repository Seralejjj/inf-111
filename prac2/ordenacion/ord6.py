def leer():
    n, i, j = map(int, input().split())
    v = list(map(int, input().split()))
    return v, i, j

def ord_rango(v, i, j):
    v[i:j+1] = sorted(v[i:j+1])

def mostrar(v):
    print(' '.join(map(str, v)))

v, i, j = leer()
ord_rango(v, i, j)
mostrar(v)