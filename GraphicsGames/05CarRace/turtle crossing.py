from turtle import Screen
from my_turtle import MyTurtle
from car import Car
from statement import Statement
import time

road = Screen()
road.setup(width=600, height=600)
road.bgcolor("blue")
road.tracer(0)

turtle= MyTurtle()
cars = []
for _ in range(10):
    _ = Car()
    cars.append(_)

show = Statement()

road.listen()
road.onkey(turtle.move_forward,'Up')

go= True
s_time = 0.1
while go:
    road.update()
    time.sleep(s_time)
    for each in cars:
        each.move()

        if each.xcor() < -300:
            each.reset()
            
        
        elif turtle.distance(each) < 25:
            go = False

    if turtle.ycor() > 280 :
        turtle.reset()
        show.icr_level()
        


    
    
show.show()   

    






road.exitonclick()