from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)

"""
More efficent way to do the above:
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
"""








screen = Screen()
screen.exitonclick()
