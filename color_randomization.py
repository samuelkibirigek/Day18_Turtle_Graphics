import turtle as t
import random

timmy = t.Turtle()
timmy.pensize(3)
timmy.speed("fastest")
t.colormode(255)

angles = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_generated = (r, g, b)
    return color_generated


for _ in range(200):
    timmy.color(random_color())
    timmy.setheading(random.choice(angles))
    timmy.forward(10)


screen = t.Screen()
screen.exitonclick()

