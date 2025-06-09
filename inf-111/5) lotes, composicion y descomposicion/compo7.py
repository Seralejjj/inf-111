a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

while b != 0:
    resto = a % b  
    a = b
    b = resto

print(f"El máximo común divisor es {a}")