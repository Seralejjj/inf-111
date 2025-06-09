def contar_apariciones(X, N):
    contador = 0
    for digito in str(N):
        if int(digito) == X:
            contador += 1
    return contador

X = int(input())
N = int(input())

print(contar_apariciones(X, N))