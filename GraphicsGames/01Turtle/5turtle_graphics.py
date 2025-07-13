import turtle
from random import randint
my_turtle = turtle.Turtle()
my_turtle.speed('fastest')

def random_color():
    r =randint(0,1)
    g= randint(0,1)
    b= randint(0,1)
    color = (r , g , b)
    return color

# my code
for i in range(0,360,5):
    my_turtle.pencolor(random_color())
    my_turtle.seth(90+i)
    my_turtle.circle(100)

# suggested
# for i in range(360 // 5):
#     my_turtle.pencolor(random_color())
#     my_turtle.seth(my_turtle.heading()+i)
#     my_turtle.circle(100)


my_screen = turtle.Screen()
my_screen.exitonclick()