from turtle import Turtle, Screen
import random

timmy = Turtle()
direction = ["m_forward", "m_back", "m_left", "m_right"]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy.pensize(3)
timmy.speed("fastest")
angles = [0, 90, 180, 270]

#This commented out code is a longer process that does not use sethead method
# def forward():
#     timmy.right(180)
#     timmy.forward(10)
#
#
# def back():
#     timmy.left(180)
#     timmy.forward(10)
#
#
# def left():
#     timmy.left(90)
#     timmy.forward(10)
#
#
# def right():
#     timmy.right(90)
#     timmy.forward(10)
#
# for _ in range(100):
#     move = random.choice(direction)
#     change_color = random.choice(colours)
#     timmy.color(change_color)
#     if move == "m_forward":
#         forward()
#     elif move == "m_back":
#         back()
#     elif move == "m_right":
#         right()
#     elif move == "m_left":
#         left()

#the shorter method
for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.setheading(random.choice(angles))
    timmy.forward(10)


screen = Screen()
screen.exitonclick()

