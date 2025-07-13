from turtle import Turtle, Screen
from random import choice

colors = ["red", "green", "blue", "cyan"]
my_turtle = Turtle()


my_turtle.color(choice(colors))
for i in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)

for i in range(3):
    my_turtle.forward(100)
    my_turtle.right(120)


my_turtle.color(choice(colors))
for i in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)


my_turtle.color(choice(colors))
for i in range(5):
    my_turtle.forward(100)
    my_turtle.left(72)

for i in range(5):
    my_turtle.forward(100)
    my_turtle.right(72)


my_turtle.color(choice(colors))
for i in range(6):
    my_turtle.forward(100)
    my_turtle.left(60)

for i in range(6):
    my_turtle.forward(100)
    my_turtle.right(60)


my_turtle.color(choice(colors))
for i in range(8):
    my_turtle.forward(100)
    my_turtle.left(45)

for i in range(8):
    my_turtle.forward(100)
    my_turtle.right(45)


my_turtle.color(choice(colors))
for i in range(10):
    my_turtle.forward(100)
    my_turtle.left(36)

for i in range(10):
    my_turtle.forward(100)
    my_turtle.right(36)








my_screen = Screen()
my_screen.exitonclick()