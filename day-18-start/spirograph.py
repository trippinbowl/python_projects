# import turtle
# import random
#
# tim = turtle.Turtle()
# screen = turtle.Screen()
#
# tim.speed("fastest")
# screen.colormode(255)
#
#
# for spirals in range(0, 500):
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     tim.pensize(2)
#     tim.pencolor(r, g, b)
#
#     tim.circle(100)
#     tim.left(5)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(9)