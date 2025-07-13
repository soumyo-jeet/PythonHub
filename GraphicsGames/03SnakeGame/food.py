from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.penup()
        self.fillcolor('blue')
        self.originate()

    def originate(self):
        x_cor = randint(-280,280)
        y_cor = randint(-280,280)
        self.goto(x_cor,y_cor)




