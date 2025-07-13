from turtle import Turtle, Screen
from random import randint , choice
my_turtle = Turtle()
colors = ["red", "green", "blue", "cyan"]
my_turtle.width(20)

for i in range(180):
    movement = choice([0, 90, 180, 270])
    my_turtle.color(choice(colors))
    my_turtle.forward(25)
    my_turtle.seth(movement)










my_screen = Screen()
my_screen.exitonclick()