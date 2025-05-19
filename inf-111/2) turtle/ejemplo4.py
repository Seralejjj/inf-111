import turtle

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  
screen.bgcolor("yellow")         
screen.title("Iniciales S T")

t = turtle.Turtle()
t.speed(3)
t.pensize(10)
t.color("black")

def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Dibujar la S
mover(-150, 100)
t.setheading(165)
t.circle(40, 180)
t.circle(-40, 180)

# Dibujar la T más abajo todavía
mover(-20, -50)  # Antes era 0, ahora bajé a -50
t.setheading(90)
t.forward(150)    # Línea vertical hacia arriba
mover(-60, 100)   # Línea horizontal
t.setheading(0)
t.forward(80)     # Línea horizontal de la T

t.hideturtle()
turtle.done()
