from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
screen = Screen()

# tim.shape("turtle")
# tim.shapesize(2)
# tim.color("red")
# tim.pensize(2)
#
# for item in range(0, 8):
#     tim.forward(50)
#     tim.left(45)

# Draw a dashed line
tim.shape("arrow")
#tim.shapesize(5)
tim.color("red")
tim.pensize(5)

for item in range(0, 15):
    if item % random.randint(2, 3) == 0:
        tim.color("green")
    else:
        tim.color("blue")
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


# tim.forward(50)
# tim.teleport(50)

screen.exitonclick()
