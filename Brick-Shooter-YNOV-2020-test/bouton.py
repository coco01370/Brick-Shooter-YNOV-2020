import turtle
import tkinter

pen = turtle.Turtle()
pen.hideturtle()

for i in range(2):
    pen.forward(80)
    pen.left(90)
    pen.forward(30)
    pen.left(90)
    
pen.penup()
pen.goto(7, 6)
pen.write("Click Me!", font=("Arial",12,"normal"))

def btnclick(x, y):
    if x > 0 and x <81 and y > 0 and y < 30:
        quit()

turtle.onscreenclick(btnclick, 1)
turtle.listen()

turtle.done()