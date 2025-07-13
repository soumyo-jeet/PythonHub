from turtle import Turtle, Screen

my_turtle = Turtle()

for i in range (10):
    my_turtle.forward(10)
    my_turtle.up()
    my_turtle.forward(10)
    my_turtle.down()



my_screen = Screen()
my_screen.exitonclick()