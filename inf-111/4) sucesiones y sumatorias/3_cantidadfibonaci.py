a = int(input("Ingrese el número a: "))
b = int(input("Ingrese el número b: "))

anterior = 0
actual = 1
contador = 0 

if a <= 0 <= b:
    contador += 1

while actual <= b:
    if actual >= a:
        contador += 1
    siguiente = anterior + actual
    anterior = actual
    actual = siguiente

print("Cantidad de Fibonacci entre", a, "y", b, ":", contador)