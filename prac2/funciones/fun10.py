def contar_barcos(a, b):
    barcos = 0
    while b != 0:
        barcos += a // b
        a, b = b, a % b
    return barcos

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(contar_barcos(a, b))