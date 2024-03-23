import turtle
import random

# Initialize the turtle module
tim = turtle.Turtle()
screen = turtle.Screen()
color = ["DarkBlue", "yellow", "violet", "SeaGreen", "red4"]

for n in range(3, 15):
    angle = 360 / n
    tim.pensize(3)
    tim.pencolor(random.choice(color))

    for i in range(n):
        tim.forward(100)
        tim.right(angle)


screen.exitonclick()


