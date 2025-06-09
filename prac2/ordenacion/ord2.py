def leer():
    n = int(input())
    return [input().split() for _ in range(n)]

def nombres(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j][0] > lst[j+1][0]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def apellidos(lst, ini, fin):
    for i in range(ini, fin):
        for j in range(ini, fin-1):
            if lst[j][1] < lst[j+1][1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def ordenar(lst):
    nombres(lst)
    i = 0
    while i < len(lst):
        j = i
        while j < len(lst) and lst[j][0] == lst[i][0]:
            j += 1
        if j-i > 1:
            apellidos(lst, i, j)
        i = j

def mostrar(lst):
    for n, a in lst:
        print(n, a)

est = leer()
ordenar(est)
mostrar(est)