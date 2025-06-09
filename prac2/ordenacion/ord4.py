def leer():
    n = int(input())
    v = list(map(int, input().split()))
    k = int(input())
    return v, k

def ord_grupos(v, k):
    for i in range(0, len(v), k):
        fin = min(i+k, len(v))
        v[i:fin] = sorted(v[i:fin])

def ord_inter(v, k):
    for i in range(k, len(v), 2*k):
        fin = min(i+k, len(v))
        v[i:fin] = sorted(v[i:fin], reverse=True)

def mostrar(v):
    print(*v)

v, k = leer()
ord_grupos(v, k)
ord_inter(v, k)
mostrar(v)