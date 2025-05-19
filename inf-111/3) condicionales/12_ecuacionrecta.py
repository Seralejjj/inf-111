import math

x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

# Calcular la pendiente (m)
if x2 != x1:  # Evitar división por cero
    m = (y2 - y1) / (x2 - x1)
    # Calcular la ordenada al origen (b)
    b = y1 - m * x1

    # Ecuación de la recta en forma pendiente-intersección: y = m*x + b
    print(f"Ecuación pendiente-intersección: y = {m}*x + {b}")

    # Para pasar a la forma general Ax + By + C = 0
    # Movemos todo a un lado: m*x - y + b = 0 => A = m, B = -1, C = b
    A = m
    B = -1
    C = b

    print(f"Ecuación general de la recta: {A}x + {B}y + {C} = 0")

else:
    # Caso para recta vertical x = c
    print(f"La recta es vertical y su ecuación es: x = {x1}")
