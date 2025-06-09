def cambiar_bit(N, k):
    binario = []
    temp = N
    for _ in range(8):
        binario.append(temp % 2)
        temp = temp // 2
    binario = binario[::-1]
    
    pos = 8 - k
    if 0 <= pos < 8:
        binario[pos] = 1 if binario[pos] == 0 else 0
    
    nuevo_num = 0
    for i in range(8):
        nuevo_num += binario[i] * (2 ** (7 - i))
    return nuevo_num

N, k = map(int, input().split())
print(cambiar_bit(N, k))