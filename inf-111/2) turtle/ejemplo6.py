import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("#0a1128")
screen.title("Paisaje Nocturno - Dibujo Rápido")

t = turtle.Turtle()
t.speed(0) 
t.hideturtle()
t.pensize(2)
t.showturtle() 

def dibujar_estrella(x, y, tamaño):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(tamaño)
        t.right(144)
    t.end_fill()

def dibujar_arbol_simple(x, y, altura):
    # Tronco
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#5e3023")
    t.begin_fill()
    for _ in range(2):
        t.forward(15)
        t.left(90)
        t.forward(altura)
        t.left(90)
    t.end_fill()
    
    # Copa
    t.penup()
    t.goto(x-25, y+altura)
    t.pendown()
    t.color("#2d5a27")
    t.begin_fill()
    for _ in range(3):
        t.forward(65)
        t.left(120)
    t.end_fill()

def dibujar_montana_simple(x, y, ancho, altura):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#3a4e60")
    t.begin_fill()
    t.goto(x + ancho/2, y + altura)
    t.goto(x + ancho, y)
    t.goto(x, y)
    t.end_fill()

t.penup()
t.goto(-180, 180)
t.pendown()
t.color("#f5f3ce")
t.begin_fill()
t.circle(40)
t.end_fill()

for _ in range(15):
    dibujar_estrella(
        random.randint(-380, 380),
        random.randint(100, 350),
        random.uniform(3, 6)
    )

dibujar_montana_simple(-400, -150, 300, 200)
dibujar_montana_simple(-150, -150, 300, 250)
dibujar_montana_simple(100, -150, 350, 180)

for x in range(-350, 400, 100):
    dibujar_arbol_simple(x, -150, random.randint(40, 100))

# Lago
t.penup()
t.goto(100, -250)
t.pendown()
t.color("#1e3f66")
t.begin_fill()
t.circle(70)
t.end_fill()

# Reflejo
t.penup()
t.goto(120, -270)
t.pendown()
t.color("#3a638c")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(0, -320)
t.color("white")
t.write("", align="center", font=("Arial", 16, "bold"))

t.hideturtle()
turtle.done()