import turtle
import random

# Initialize the turtle module and screen
tim = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)  # Set color mode to accept RGB values
new_color = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
random_turn = [tim.left, tim.right]

def random_walk(steps):
    tim.pensize(10)
    # tim.speed("fastest")  # Uncomment for faster drawing

    for _ in range(steps):
        # Generate random color for each step
        color = random.choice(new_color)

        # Random step size between 10 and 30
        step_size = random.randint(10, 30)

        # Choose a random turn function and a random turning angle
        turn_function = random.choice(random_turn)
        angle = random.randint(-90, 90)  # Updated to choose a random angle for each step

        # Set the pen color and move the turtle
        tim.pencolor(color)
        tim.forward(step_size)
        turn_function(angle)

# Execute the random walk with 200 steps
random_walk(200)

# Exit on click
screen.exitonclick()
