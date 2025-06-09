def leer():
    return list(map(int, input().split()))

def unir(v1, v2):
    return v1 + v2

def ordenar(v):
    return sorted(v)

def imprimir(v):
    print('\n'.join(map(str, v)))

n, m = map(int, input().split())
a = leer()
b = leer()
c = ordenar(unir(a, b))
imprimir(c)