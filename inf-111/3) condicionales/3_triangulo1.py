import math

# inicio
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# proceso
pi = math.pi
conversion = pi / 180
c_rad = c * conversion

c2 = a**2 + b**2 - 2 * a * b * math.cos(c_rad)

if c2 >= 0:
    c = math.sqrt(c2)
# imprimir el resultado
    print("El valor de c es:", c)
else:
    print("No es posible calcular c, ya que c2 es negativo.")

