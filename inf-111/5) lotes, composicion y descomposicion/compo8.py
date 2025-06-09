n = int(input())
original = n
contador = 0
temporal = 1

while temporal * 10 <= n:
    temporal *= 10

while temporal > 0:
    digito = n // temporal
    n = n % temporal
    temporal = temporal // 10
    
    if digito != 0 and original % digito == 0:
        contador += 1

print(contador)