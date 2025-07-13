from turtle import Turtle

class Statement(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.level = 1
        self.level_show()

    def icr_level(self):
        self.level += 1
        self.clear()
        self.level_show()

    def level_show(self):
        self.goto(-250, 250)
        self.write(arg= f"level : {self.level}", align='center' , font=("Arial" , 15 , "normal"))


    def show(self):
        self.goto(0,0)
        self.write(arg= "Game Over.", align='center' , font=("Arial" , 15 , "normal"))