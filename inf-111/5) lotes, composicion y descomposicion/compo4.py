n = int(input("Ingrese n (1 ≤ n ≤ 10000): "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

while factorial > 0:
    digito = factorial % 10
    if digito != 0:
        break
    factorial = factorial // 10
    
print("El último dígito distinto de cero es:", digito)