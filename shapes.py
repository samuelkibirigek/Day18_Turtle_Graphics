from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colors = ["black", "brown", "pink", "green", "purple", "yellow", "blue", "grey", "red"]
sides = 3

while sides < 10:
    angle = int(360 / sides)
    timmy.color(random.choice(colors))
    for _ in range(sides):
        timmy.right(angle)
        timmy.forward(100)
    sides += 1

screen = Screen()
screen.exitonclick()
