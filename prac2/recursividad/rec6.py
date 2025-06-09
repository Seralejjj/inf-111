def suma_cuadrados(n):
    if n == 0:
        return 0
    else:
        return n*n + suma_cuadrados(n-1)

n= int(input("Ingrese N: "))
resultado = suma_cuadrados(n)
print(resultado)