import turtle

screen = turtle.Screen()
screen.title("Figuras Coloridas en Orden Específico")
t = turtle.Turtle()
t.speed(5)

def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def dibujar_triangulo(x, y, tamaño):
    mover(x, y)
    t.color("cyan", "cyan")
    t.begin_fill()
    for _ in range(3):
        t.forward(tamaño)
        t.left(120)
    t.end_fill()

def dibujar_cuadrado(x, y, tamaño):
    mover(x, y)
    t.color("red", "red")
    t.begin_fill()
    for _ in range(4):
        t.forward(tamaño)
        t.left(90)
    t.end_fill()

def dibujar_rectangulo(x, y, ancho, alto):
    mover(x, y)
    t.color("yellow", "yellow")
    t.begin_fill()
    for _ in range(2):
        t.forward(ancho)
        t.left(90)
        t.forward(alto)
        t.left(90)
    t.end_fill()

def dibujar_circulo(x, y, radio):
    mover(x, y - radio)
    t.color("green", "green")
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

def dibujar_ovalo(x, y, ancho, alto):
    mover(x, y)
    t.color("red", "red")
    t.begin_fill()
    for _ in range(2):
        t.circle(alto // 2, 90)
        t.forward(ancho)
        t.circle(alto // 2, 90)
    t.end_fill()

def dibujar_trapecio(x, y, base_mayor, base_menor, altura):
    mover(x, y)
    t.color("green", "green")
    t.begin_fill()
    t.forward(base_mayor)
    t.right(135)
    t.forward(altura * 1.414)  
    t.right(45)
    t.forward(base_menor)
    t.right(45)
    t.forward(altura * 1.414)
    t.end_fill()

def dibujar_paralelogramo(x, y, ancho, alto, inclinacion):
    mover(x, y)
    t.color("cyan", "cyan")
    t.begin_fill()
    t.forward(ancho)
    t.left(inclinacion)
    t.forward(alto)
    t.left(180 - inclinacion)
    t.forward(ancho)
    t.left(inclinacion)
    t.forward(alto)
    t.end_fill()

def dibujar_rombo(x, y, diagonal_mayor, diagonal_menor):
    mover(x, y)
    t.color("yellow", "yellow")
    t.begin_fill()
    t.right(45)
    t.forward(diagonal_menor // 2)
    t.right(90)
    t.forward(diagonal_mayor // 2)
    t.right(90)
    t.forward(diagonal_menor // 2)
    t.right(90)
    t.forward(diagonal_mayor // 2)
    t.end_fill()

dibujar_triangulo(-200, 100, 80)       
dibujar_cuadrado(-50, 100, 80)           
dibujar_rectangulo(100, 100, 100, 60)     
dibujar_circulo(250, 100, 40)            

dibujar_ovalo(250, -50, 60, 40)          
dibujar_trapecio(100, -50, 100, 60, 40)  
dibujar_paralelogramo(-50, -50, 80, 60, 60)
dibujar_rombo(-200, -50, 80, 60)       

t.hideturtle()
turtle.done()
