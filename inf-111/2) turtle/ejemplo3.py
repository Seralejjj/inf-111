import turtle
import math

def dibujar_circulo(x, y, radio):
    turtle.penup()
    turtle.goto(x, y - radio)  
    turtle.pendown()
    turtle.circle(radio)  
    area = math.pi * (radio ** 2)  
    turtle.penup()
    turtle.goto(x, y)  
    turtle.write(f'Área: {area:.2f}', align='center', font=('Arial', 12, 'normal'))
    turtle.pendown()

x = float(input("Ingrese las coordenadas del centro del círculo (x): "))
y = float(input("Ingrese las coordenadas del centro del círculo (y): "))
radio = float(input("Ingrese el radio del círculo: "))

turtle.speed(1)
dibujar_circulo(x, y, radio)

turtle.done()
