def encontrar_ocurrencias(a, b):
    len_a = len(a)
    ocurrencias = []
    for i in range(len(b) - len_a + 1):
        if b[i:i+len_a] == a:
            ocurrencias.append((i, i + len_a - 1))
    return ocurrencias

a = input().strip()
b = input().strip()

resultados = encontrar_ocurrencias(a, b)
for ocurrencia in resultados:
    print(ocurrencia)