import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_color = (r, g, b)
    return generated_color


def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

spirograph(5)
screen = t.Screen()
screen.exitonclick()