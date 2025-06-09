# Forma Iterativa de izquierda a derecha
def suma_iterativaI(v, a, b):
    s = 0
    for i in range(a, b + 1):
        s += v[i]
    return s

# Forma Recursiva de izquierda a derecha
def suma_recursivaI(v, a, b):
    if a > b:
        return 0
    return v[a] + suma_recursivaI(v, a + 1, b)
