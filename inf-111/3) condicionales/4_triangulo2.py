import math

# inicio
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))
x3 = float(input("Ingrese x3: "))
y3 = float(input("Ingrese y3: "))

# procesos
a = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)  
b = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)  
c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) 

if (a + b > c) and (a + c > b) and (b + c > a):
# Cálculo de ángulos
    angulo_a = math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * (180 / math.pi)  
    angulo_b = math.acos((a**2 + c**2 - b**2) / (2 * a * c)) * (180 / math.pi)  
    angulo_c = 180 - angulo_a - angulo_b 

    perimetro = a + b + c

    s = perimetro / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# Imprimir
    print("Lados: a =", a, ", b =", b, ", c =", c)
    print("Ángulos: A =", angulo_a, "grados, B =", angulo_b, "grados, C =", angulo_c, "grados")
    print("Perímetro:", perimetro)
    print("Área:", area)
else:
    print("No es un triángulo")
