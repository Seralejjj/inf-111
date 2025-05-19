import turtle
def draw_arrow(color, x, y, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle. setheading(angle)
    turtle.pendown ()
    turtle.pensize(5)
    turtle.pencolor(color)
    turtle.forward(50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.right(150)
    turtle.forward(15)
    turtle.backward(15)
    turtle.left(300)
    turtle. forward(15)
    turtle.backward(15)
    turtle.right(150)
    turtle.end_fill()

turtle.speed(3)
draw_arrow("red", 0, 0, 0) 
draw_arrow("blue", -50, 50, 270) 
draw_arrow("green", 0, 100, 180) 
draw_arrow("orange", 50, 50, 90)

turtle.hideturtle()
turtle.done()



