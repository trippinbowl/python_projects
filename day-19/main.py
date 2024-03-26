import turtle

tim = turtle.Turtle()
tom = turtle.Turtle()
john = turtle.Turtle()
dodo = turtle.Turtle()
screen = turtle.Screen()


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def fwd():
    tim.forward(10)


def bck():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(fwd, "w")
screen.onkeypress(bck, "s")
screen.onkeypress(clear, "c")
screen.listen()


tom.forward(200)
john.right(90)
john.forward(200)
dodo.left(90)
dodo.forward(200)



screen.exitonclick()