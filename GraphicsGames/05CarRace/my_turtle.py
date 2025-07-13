from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0 , -280)
        self.seth(90)

    def move_forward(self):
        self.forward(20)

    def reset(self):
        self.goto(0,-280)

    
