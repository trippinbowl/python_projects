# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)

# import turtle
# import random
#
#
# def left_turn():
#     tim.left(90)
#     tim.forward(25)
#     tim.left(90)
#
#
# def right_turn():
#     tim.right(90)
#     tim.forward(50)
#     tim.right(90)
#
#
# tim = turtle.Turtle()
# screen = turtle.Screen()
#
# new_color = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# screen.colormode(255)
#
# for i in range(0, 24):
#     random_color = random.choice(new_color)
#     tim.pencolor(random_color)
#     tim.dot(15)
#     tim.forward(50)
#     if i % 6 == 0 and i % 12 != 0:
#         left_turn()
#     elif i % 12 == 0:
#         right_turn()
#
#
#
# screen.exitonclick()


import turtle
import random

tim = turtle.Turtle()
screen = turtle.Screen()

new_color = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
screen.colormode(255)
tim.speed("fast")  # Speed up the drawing
tim.penup()  # Lift the pen to move without drawing
tim.hideturtle()

# Start position
tim.goto(-200, 200)

for y in range(10):  # 5 lines
    for x in range(10):  # 5 dots per line
        tim.dot(25, random.choice(new_color))
        tim.forward(50)  # Space between dots
    # Move to the beginning of the next line
    tim.backward(50 * 10)  # Go back to the start of the line
    tim.right(90)
    tim.forward(50)
    tim.left(90)

screen.exitonclick()


