def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mostrar_primos_con_posiciones():
    numeros = list(map(int, input().split(',')))
    for i, num in enumerate(numeros):
        if es_primo(num):
            print(num, i, end=' ')

mostrar_primos_con_posiciones()