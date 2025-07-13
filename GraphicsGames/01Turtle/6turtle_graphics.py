from turtle import Turtle, Screen
import random


color_list = ["red", "green", "blue", "cyan"]

my_turtle= Turtle()
my_turtle.speed('fastest')
my_turtle.hideturtle()
my_turtle.pos()
my_turtle.penup()
my_turtle.goto(-300, -250)

    

def printing():
    for _ in range (10):
        color = random.choice(color_list)
        my_turtle.dot(20 , color)
        my_turtle.forward(58)

for _ in range (10):
    printing()
    my_turtle.backward(10 * 58)
    my_turtle.seth(90)
    my_turtle.forward(58)
    my_turtle.seth(0)




my_screen = Screen()
my_screen.exitonclick