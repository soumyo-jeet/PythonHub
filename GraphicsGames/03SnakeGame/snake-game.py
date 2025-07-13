from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

FONT = ("Arial" , 15 , "bold")

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score_board = ScoreBoard()
head = my_snake.head



go = True
while go:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()
    if head.xcor() >= 300 or head.xcor() <= -300 or head.ycor() >= 300 or head.ycor() <= -300:
        go = False

    for seg in my_snake.segment[1:]:
        if head.distance(seg) < 10 :
            go = False

    if head.distance(my_food) < 10 :
        my_food.originate()
        my_snake.extend_body()
        my_score_board.incr_score()


statement = Turtle()
statement.color("white")
statement.hideturtle()
statement.write(arg= "Game Over.", align= "Center", font= FONT)

    




my_screen.exitonclick()
