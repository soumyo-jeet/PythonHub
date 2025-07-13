from turtle import Turtle
from random import randint, choice
COLORS = ['red' , 'yellow' , 'white' , 'green']
POS = [300,320,340,360,380,400]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len= 4, stretch_wid=1)
        self.penup()
        self.move_by = 10
        self.reset()
        
    def icr_speed(self):
        self.move_by -=5     

    def move(self):
        pos = self.xcor() - self.move_by
        self.goto(pos, self.y_cor)

    def reset(self):
        self.x_cor = choice(POS)
        self.y_cor = randint(-250,250)
        self.colors = choice(COLORS)
        self.color(self.colors)
        self.goto(self.x_cor, self.y_cor)


