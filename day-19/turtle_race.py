# import turtle
# import random
#
# is_race_on = False
# screen = turtle.Screen()
# screen.setup(500, 400)
# user_bet = screen.textinput("Make your bet", "Choose your Turtle color: ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# coordinates = [(-230, 125), (-230, 75), (-230, 25), (-230, -25), (-230, -75), (-230, -125)]
# # random_coordinates = random.choice(coordinates)
#
# all_turtles = []
#
# for index in range(0, 6):
#     new_turtle = turtle.Turtle(shape="turtle")
#     new_turtle.color(colors[index])
#     new_turtle.penup()
#     new_turtle.goto(coordinates[index])
#     all_turtles.append(new_turtle)
#
# if user_bet:
#     is_race_on = True
#
# distance_travelled = 0
#
# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You chose {user_bet}, and it is the winning turtle! Congratulations!")
#             else:
#                 print(f"You chose {user_bet}, but unfortunately {winning_color} is the winning turtle! You lose!")
#
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)
#         distance_travelled += rand_distance
#
# screen.exitonclick()

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(500, 400)

# Ask for user's bet on turtle color
user_bet = screen.textinput("Make your bet", "Which turtle color will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")

# Initialize turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
directions = [0, 60, 120, 180, 240, 300]  # Different directions for the turtles
turtles = []

# Draw the finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(0, 0)
# finish_line.right(90)
finish_line.dot()
finish_line.backward(200)
finish_line.right(90)
finish_line.pendown()
finish_line.circle(200)  # Draw a circle with a radius of 200 units as the finish line
finish_line.hideturtle()  # Hide the turtle used to draw the finish line

for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(0, 0)  # Start from the center
    new_turtle.setheading(directions[i])
    turtles.append(new_turtle)

# Start the race
is_race_on = bool(user_bet)

def is_out_of_bounds(turtle):
    # Checks if the turtle has crossed the finish line (circle radius)
    return turtle.distance(0, 0) > 200

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))

        if is_out_of_bounds(turtle):
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()


